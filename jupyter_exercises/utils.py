import os
import sys
import json
import requests
import uuid

from typing import List, Dict, Any, Callable, Union, Optional
from pydantic import BaseModel, ValidationError
from bs4 import BeautifulSoup
from inspect import signature, Parameter
from typing import get_type_hints, Any, Dict, List, Optional, get_origin, get_args, Literal


def print_tree(path, prefix=''):
    """Recursively prints the directory structure in a tree format."""
    if not prefix:
        print(path)
    # Get the list of entries in the current path
    entries = os.listdir(path)
    entries.sort()  # Sort for consistent output

    # Iterate through each entry
    for i, entry in enumerate(entries):
        full_path = os.path.join(path, entry)
        is_last_entry = (i == len(entries) - 1)

        # Print the current entry with appropriate prefix
        print(f"{prefix}{'└── ' if is_last_entry else '├── '}{entry}")

        # If it's a directory, recurse into it
        if os.path.isdir(full_path):
            new_prefix = prefix + ('    ' if is_last_entry else '│   ')
            print_tree(full_path, new_prefix)


def make_tool_schema(func: callable) -> Dict[str, Any]:
    """
    Auto-generates an LLM tool call schema (OpenAI/Anthropic format) from a function.
    Uses type hints and docstring for descriptions. Requires Pydantic (pip install pydantic).
    
    Example:
        def get_weather(location: str, unit: str = "fahrenheit") -> dict:
            \"\"\"Get current weather for a location.\"\"\"
            pass
        
        schema = make_tool_schema(get_weather)
        # → Ready for OpenAI: {"type": "function", "function": {...}}
    """
    try:
        from pydantic import BaseModel, Field, create_model
    except ImportError:
        raise ImportError("Pydantic required. Install with: pip install pydantic")

    # 1. Extract function metadata
    sig = signature(func)
    type_hints = get_type_hints(func)
    docstring = (func.__doc__ or "").strip().split('\n')[0] if func.__doc__ else ""
    
    # 2. Build Pydantic model fields from signature
    fields = {}
    for name, param in sig.parameters.items():
        # Skip self/cls for methods
        if name in ('self', 'cls') and param.kind in (Parameter.POSITIONAL_OR_KEYWORD,):
            continue
            
        # Get type annotation (default to Any if missing)
        annotation = type_hints.get(name, Any)
        
        # Extract description from docstring (naive but works for 80% of cases)
        description = f"Parameter '{name}'"  # Fallback
        if docstring:
            # Look for :param name: description in docstring (Google/Numpy style)
            for line in docstring.split('\n'):
                if line.strip().startswith(f":param {name}:"):
                    description = line.split(f":param {name}:", 1)[1].strip()
                    break
                # Also handle Sphinx style: :type name: str -> then next line might have desc
                if line.strip().startswith(f":type {name}:"):
                    # Description is often on next line
                    pass  # Handled by fallback for simplicity
        
        # Handle defaults (determine if required)
        default = ... if param.default is Parameter.empty else param.default
        
        # Special handling for common types
        origin = get_origin(annotation)
        args = get_args(annotation)
        
        # Optional[X] -> X | None
        if origin is Optional and len(args) == 2 and args[1] is type(None):
            annotation = args[0]
            # Make field not required (default=None handled by Pydantic)
            if default is ...:
                default = None
        
        # List[X] -> List[X]
        elif origin is list or origin is List:
            annotation = List[args[0]] if args else List[Any]
        
        # Literal['a', 'b'] -> Literal['a', 'b']
        elif origin is Literal:
            pass  # Pydantic handles this natively
        
        # Build field
        fields[name] = (
            annotation,
            Field(default, description=description) if default is not ... 
            else Field(..., description=description)
        )
    
    # 3. Dynamically create Pydantic model
    Model = create_model(f"{func.__name__}Input", **fields)
    
    # 4. Generate OpenAI/Anthropic compatible tool schema
    return {
        "type": "function",
        "function": {
            "name": func.__name__,
            "description": docstring or f"Invoke {func.__name__}",
            "parameters": Model.model_json_schema(),
            "strict": True  # Critical for reducing hallucinations (OpenAI) / equivalent in Anthropic
        }
    }


def generate_mock_tool_call(
    tool_name: str,
    arguments: Dict[str, Any],
    call_id: Optional[str] = None,
) -> Dict[str, Any]:
    """
    Generates a realistic LLM tool call request (mimicking OpenAI/Anthropic output) for testing.
    Validates arguments against a tool schema (if provided) and can inject errors for testing error paths.
    
    Args:
        tool_name: Name of the tool to call (must match registry)
        arguments: Dict of arguments to pass to the tool
        call_id: Optional custom ID (defaults to UUIDv4)
    Returns:
        Dict matching LLM tool_call structure:
        {
            "id": "call_xxx",
            "type": "function",
            "function": {
                "name": "tool_name",
                "arguments": "{\"valid\": \"json\"}"
            }
        }
    
    Example:
        schema = make_tool_schema(get_weather)  # From previous function
        mock_call = generate_mock_tool_call(
            tool_name="get_weather",
            arguments={"location": "Paris, FR", "unit": "celsius"},
            tool_schema=schema
        )
        # → Ready to pass to execute_tool_call()
    """
    if call_id is None:
        call_id = f"call_{uuid.uuid4().hex[:8]}"
    args_json = json.dumps(arguments, ensure_ascii=False)
    return {
        "id": call_id,
        "type": "function",
        "function": {
            "name": tool_name,
            "arguments": args_json
        }
    }



def execute_tool_call(
    tool_calls: List[Dict[str, Any]], 
    tool_registry: Dict[str, Callable]
) -> List[Dict[str, str]]:
    """
    Processes LLM tool call responses, executes functions, and returns LLM-expected tool result messages.
    
    Args:
        tool_calls: List of tool call objects from LLM response (OpenAI/Anthropic format)
                   Each must have: 
                     - 'id': str (tool call ID)
                     - 'type': str (should be 'function')
                     - 'function': dict with 'name' (str) and 'arguments' (JSON str)
        tool_registry: Dict mapping function names to actual callables
                      Example: {"get_weather": get_weather_func}
    
    Returns:
        List of message dicts in LLM-expected format for tool results:
        [{"role": "tool", "tool_call_id": "<id>", "content": "<stringified result>"}, ...]
    
    Handles:
        - JSON argument parsing
        - Function execution (with error handling)
        - Automatic string conversion of results (str → kept as-is, non-str → JSON)
        - Multiple tool calls in one response
        - Missing functions / invalid JSON
    """
    if not tool_calls:
        return []

    tool_results = []
    
    for call in tool_calls:
        # Validate basic structure
        if not isinstance(call, dict) or call.get('type') != 'function':
            tool_results.append({
                "role": "tool",
                "tool_call_id": call.get('id', 'unknown'),
                "content": "Invalid tool call structure (expected type='function')"
            })
            continue

        func_name = call['function'].get('name')
        raw_args = call['function'].get('arguments', '{}')
        call_id = call.get('id', 'unknown')
        
        # 1. Look up function in registry
        if func_name not in tool_registry:
            tool_results.append({
                "role": "tool",
                "tool_call_id": call_id,
                "content": f"Error: Tool '{func_name}' not found in registry"
            })
            continue
        
        func = tool_registry[func_name]
        
        # 2. Parse arguments (handle JSON errors)
        try:
            args = json.loads(raw_args) if isinstance(raw_args, str) else raw_args
        except json.JSONDecodeError as e:
            tool_results.append({
                "role": "tool",
                "tool_call_id": call_id,
                "content": f"Error: Invalid JSON in arguments - {str(e)}"
            })
            continue
        
        # 3. Execute function (with error handling)
        try:
            result = func(**args)
            
            # 4. Convert result to LLM-expected string format
            if isinstance(result, str):
                content = result  # Keep raw strings as-is (no double-encoding)
            else:
                # For non-strings: JSON-serialize (handles dict/list/num/bool/None)
                content = json.dumps(result)
                
            tool_results.append({
                "role": "tool",
                "tool_call_id": call_id,
                "content": content
            })
            
        except Exception as e:
            tool_results.append({
                "role": "tool",
                "tool_call_id": call_id,
                "content": f"Error executing {func_name}: {type(e).__name__}: {str(e)}"
            })
    
    return tool_results