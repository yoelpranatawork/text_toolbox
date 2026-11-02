# core/cleaner_tools.py

import unicodedata


def normalize_to_ascii(text: str) -> str:
    replacements = {
        "\u2018": "'",   # Left single quotation mark
        "\u2019": "'",   # Right single quotation mark
        "\u201c": '"',   # Left double quotation mark
        "\u201d": '"',   # Right double quotation mark
        "\u2013": "-",   # En dash
        "\u2014": "-",   # Em dash
        "\u2026": "...", # Ellipsis
        "\u00a0": " ",   # Non-breaking space
    }
    for original, replacement in replacements.items():
        text = text.replace(original, replacement)
    normalized = unicodedata.normalize("NFKD", text)
    ascii_text = normalized.encode("ascii", errors="ignore").decode("ascii")
    return ascii_text

def remove_leading_trailing_spaces(text: str) -> str:
    lines = text.splitlines(keepends=True)
    cleaned_lines = []
    for line in lines:
        if line.endswith("\r\n"):
            content = line[:-2]
            ending = "\r\n"
        elif line.endswith("\n") or line.endswith("\r"):
            content = line[:-1]
            ending = line[-1]
        else:
            content = line
            ending = ""
        cleaned_lines.append(content.strip(" \t") + ending)
    return "".join(cleaned_lines)


def remove_extra_spaces(text: str) -> str:
    lines = text.splitlines(keepends=True)
    cleaned_lines = []
    for line in lines:
        if line.endswith("\r\n"):
            content = line[:-2]
            ending = "\r\n"
        elif line.endswith(("\n", "\r")):
            content = line[:-1]
            ending = line[-1]
        else:
            content = line
            ending = ""
        parts = content.split(" ")
        cleaned_content = " ".join(
            part for part in parts if part
        )
        leading_spaces = len(content) - len(content.lstrip(" "))
        trailing_spaces = len(content) - len(content.rstrip(" "))
        cleaned_content = (
            " " * leading_spaces
            + cleaned_content
            + " " * trailing_spaces
        )
        cleaned_lines.append(cleaned_content + ending)
    return "".join(cleaned_lines)

def remove_blank_lines(text: str) -> str:
    lines = text.splitlines(keepends=True)
    kept_lines = []
    for line in lines:
        content = line.rstrip("\r\n")
        if content.strip(" \t"):
            kept_lines.append(line)
    return "".join(kept_lines)

def remove_duplicate_lines(text: str) -> str:
    lines = text.splitlines(keepends=True)
    seen = set()
    unique_lines = []
    for line in lines:
        if line.endswith("\r\n"):
            content = line[:-2]
        elif line.endswith("\n") or line.endswith("\r"):
            content = line[:-1]
        else:
            content = line
        if content not in seen:
            seen.add(content)
            unique_lines.append(line)
    return "".join(unique_lines)

def normalize_line_endings(text: str, style: str = "windows") -> str:
    line_endings = {
        "windows": "\r\n",
        "unix": "\n",
        "mac": "\r",
    }
    if style not in line_endings:
        raise ValueError(
            "Unsupported line-ending style. "
            "Choose 'windows', 'unix', or 'mac'."
        )
    normalized_text = text.replace("\r\n", "\n").replace("\r", "\n")
    return normalized_text.replace("\n", line_endings[style])

def remove_special_characters(text: str) -> str:
    return "".join(
        char
        for char in text
        if char.isalnum() or char in " \t\r\n"
    )

def remove_digits(text: str) -> str:
    return "".join(char for char in text if not char.isdigit())

def remove_tabs(text: str) -> str:
    return text.replace("\t", "")
