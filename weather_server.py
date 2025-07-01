"""Weather server module using FastMCP.

This module defines a simple weather server with a tool to get weather information for a given location.
"""

import os

from mcp.server.fastmcp import FastMCP

mcp = FastMCP(
    "weather",
    host="0.0.0.0",
    port=int(
        os.environ.get("PORT", 8000),
    ),
)


@mcp.tool()
async def get_weather(location: str) -> str:
    """Get weather for location. Mocked."""
    return "It's always sunny in New York"


if __name__ == "__main__":
    mcp.run(transport="streamable-http")
