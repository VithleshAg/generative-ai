from mcp.server.fastmcp import FastMCP

server = FastMCP("Math")

@server.tool()
def add_numbers(a: float, b: float) -> float:
    """_summary_
    Add two numbers.
    """
    return a + b

@server.tool()
def multiply_numbers(a: float, b: float) -> float:
    """_summary_
    Multiply two numbers.
    """
    return a * b

# the transport ="stdio" argument tells the server to
# use standard input/output to receive and respond to tool function calls

if __name__ == "__main__":
    server.run(transport="stdio")