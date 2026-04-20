# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Commands

```bash
# Setup
uv venv && source .venv/bin/activate
uv pip install -e .

# Run MCP server
uv run main.py

# Run tests
uv run pytest

# Run a single test file
uv run pytest tests/test_document.py
```

## Architecture

This is a **FastMCP server** that exposes Python functions as MCP tools to AI assistants.

- `main.py` — initializes the `FastMCP("docs")` server, registers tools with `mcp.tool()(fn)`, and calls `mcp.run()`
- `tools/` — each file defines plain Python functions; register them in `main.py` to expose as MCP tools
- `tests/fixtures/` — real `.docx` and `.pdf` files used for integration testing

**Adding a new tool:** define the function in `tools/`, import it in `main.py`, and call `mcp.tool()(your_function)`.

## Tool Conventions

- Use `pydantic.Field(description=...)` for all parameters — this description is what the AI sees
- All function arguments and return values must have explicit type annotations
- Docstrings must follow this four-part structure:
  1. One-line summary
  2. Detailed explanation of functionality
  3. When to use **and when not to use** the tool
  4. Usage examples with expected input/output

```python
from pydantic import Field

def my_tool(
    param1: str = Field(description="Detailed description of this parameter"),
    param2: int = Field(description="Explain what this parameter does"),
) -> str:
    """One-line summary.

    Detailed explanation of what the tool does and how it works.

    When to use:
    - Use case A
    - Use case B

    When not to use:
    - Scenario where another tool is more appropriate

    Examples:
    >>> my_tool("foo", 1)
    "result"
    """
    ...
```
