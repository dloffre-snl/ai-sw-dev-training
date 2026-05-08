  

01_rag_internals.ipynb

- Goes through making a RAG system “manually” and then shows some pointers to learn about the SotA techniques and why you’d care
    
- Common problems in rag systems
    
- Ends with a langchain production example
    

02_tools_calls.ipynb

- Tool interaction through openai api calls
    

- Optionally can use the `simply_proxy.py`​ to look at the actual http calls
    

- Completing the tool interaction with making a minimal “agentic” loop
    
- Introduce tool and model poisoning so easier to talk about risks during MCP if wanted
    

- The model poisoning doesn’t have to be tied to tool calling but I thought it fit well here
    

- I had hoped to make something that would work on the Apple Neo laptops but was unsuccessful but I have the example of using MLX to train the model to use a tool and then lie to the user about it.
    

- Showing the backend processing of the api requests and how it actually then interacts with the model
    

03_mcp_jsonrpc.ipynb

- Along with `mcp_proxy.py`​ and `mcp_server.py`​ just shows the actual protocol, I didn’t think of much more to do here but all the pieces should be there to play with mcp to answer any questions
    

  

I wen through a few iterations with these tried vibe coding things, never really liked anything that came out but this is where I landed.

  

04_prompt_engineering.ipynb

- Just goes over the common techniques with some discussion. I thought maybe going into the structured output generation would be interesting here but that felt like maybe too under the hood.
    

05_attacks_security.ipynb

- Some of this was introduced in 02_tool_calls.ipynb but goes over the prompt and control markers and basic attacks against it there, I removed things that started going to more AML spaces.
    

  

Other unmentioned files:

`config.toml`​ - Each notebook reads from this for the model and endpoint configuration

`llm_monitor.py`​ - another proxy script that was dealing with stream responses in certain agentic execution modes that I don’t use in the notebooks anymore, but kept just in case

`requirements.txt`​ - hopefully the list of necessary packages to run everything

`utils.py`​ - a couple helper functions for tool training data generation, and other utilities that the notebooks don’t use anymore but kept just in case.