from mcp.server.fastmcp import FastMCP

server = FastMCP("Weather")

@server.tool()
def get_weather(city: str) -> str:
    """_summary_
    Get the current weather for a given city.
    """
    # For demonstration purposes, we'll return a mock weather report.
    # In a real implementation, you would fetch data from a weather API.
    return "The current weather in London is sunny with a temperature of 25°C."

# streamable-http transport gives api on running while stdio transport is for running in terminal and communicating with the server via standard input/output
if __name__ == "__main__":
    server.run(transport="streamable-http")