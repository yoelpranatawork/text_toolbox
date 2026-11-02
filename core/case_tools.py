# core/case_tools.py


def to_uppercase(text: str) -> str:
    return text.upper()

def to_lowercase(text: str) -> str:
    return text.lower()

def to_title_case(text: str) -> str:
    return text.title()

def to_sentence_case(text: str) -> str:
    return text.capitalize()

def invert_case(text: str) -> str:
    return text.swapcase()
