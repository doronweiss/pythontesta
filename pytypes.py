# headlines.py
from beartype import beartype

@beartype
def headline(text: str, align: bool = True) -> str:
    if align:
        return f"{text.title()}\n{'-' * len(text)}"
    else:
        return f" {text.title()} ".center(50, "o")

print(headline("python type checking"))
print(headline("python type checking", False))
print(headline("use mypy", "center"))