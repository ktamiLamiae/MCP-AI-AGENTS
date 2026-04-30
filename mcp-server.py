from mcp.server.fastmcp import FastMCP
from langchain_tavily import TavilySearch
from dotenv import load_dotenv

load_dotenv(override=True)

# Initialisation du client de recherche
web_search_client = TavilySearch()

# Création du serveur MCP
mcp = FastMCP(
    name="mcp-server",
    host="0.0.0.0",
    port=24000
)

# Tool 1 : récupérer infos employé
@mcp.tool()
def get_employee_infos(name: str):
    """"Get info about the given employee"""
    return {
        "name": name,
        "salary": 23000,
        "seniority": 12
    }

# Tool 2 : recherche web
@mcp.tool()
def search_web(query: str):
    """"Search web for the given query"""
    results = web_search_client.invoke({"query": query})
    return results


if __name__ == "__main__":
    mcp.run(transport="streamable-http")