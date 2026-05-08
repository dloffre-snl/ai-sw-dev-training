from mcp.server.fastmcp import FastMCP

def a_tool(arg1: str):
    return f"You called a tool with {arg1}."

mcp = FastMCP('mcp_test', host='localhost', port=8000)
mcp.add_tool(a_tool)
mcp.run(transport='streamable-http')