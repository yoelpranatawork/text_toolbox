# core/developer_tools.py

import base64
import json
import ast
import urllib.parse


def minify_python_code(text: str) -> str:
    """Strips comments and docstrings from Python code using ast."""
    try:
        tree = ast.parse(text)

        def remove_docstring(node):
            if (
                node.body 
                and isinstance(node.body[0], ast.Expr) 
                and isinstance(node.body[0].value, ast.Constant) 
                and isinstance(node.body[0].value.value, str)
            ):
                node.body.pop(0)
                if not node.body:
                    node.body.append(ast.Pass())

        # Remove module-level docstring if present
        remove_docstring(tree)

        # Remove function, class, and async function docstrings
        for n in ast.walk(tree):
            if isinstance(n, (ast.FunctionDef, ast.ClassDef, ast.AsyncFunctionDef)):
                remove_docstring(n)

        return ast.unparse(tree)
    except Exception as e:
        return f"# Error cleaning Python code: {str(e)}"


def format_json(text: str) -> str:
    """Pretty prints and validates JSON text."""
    try:
        parsed = json.loads(text)
        return json.dumps(parsed, indent=4)
    except Exception as e:
        return f"Invalid JSON: {str(e)}"


def base64_encode(text: str) -> str:
    """Encodes text to Base64."""
    return base64.b64encode(text.encode("utf-8")).decode("utf-8")


def base64_decode(text: str) -> str:
    """Decodes text from Base64."""
    try:
        return base64.b64decode(text.encode("utf-8")).decode("utf-8")
    except Exception as e:
        return f"Invalid Base64: {str(e)}"


def url_encode(text: str) -> str:
    """URL encodes text."""
    return urllib.parse.quote(text)


def url_decode(text: str) -> str:
    """URL decodes text."""
    return urllib.parse.unquote(text)
