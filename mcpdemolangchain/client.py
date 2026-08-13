from click import command
from langchain_mcp_adapters.client import MultiServerMCPClient
from langgraph.prebuilt import create_react_agent
from langchain_groq import ChatGroq
from dotenv import load_dotenv
import asyncio
import sys

load_dotenv()

async def main():
    mcp_client = MultiServerMCPClient({
        "weather": {
            "url": "http://127.0.0.1:8000/mcp",
            "transport": "http"
        },
        "math": {
            "command": sys.executable,
            "args": ["mathserver.py"],   ## Ensure correct absolute path
            "transport": "stdio"
        }
    })
    
    import os
    os.environ["GROQ_API_KEY"] = os.getenv("GROQ_API_KEY")

    tools = await mcp_client.get_tools()
    model = ChatGroq(model="llama-3.3-70b-versatile")
    agent = create_react_agent(model, tools)
    
    # math_response =  await agent.ainvoke({"messages": [{"role": "user", "content": "What is 100+10*5?"}]})
    # print("Math response: ", math_response['messages'][-1].content)

    
    weather_response = await agent.ainvoke({"messages": "What is the weather in London?"})
    print("Weather response: ", weather_response['messages'][-1].content)


asyncio.run(main()) 
    