# Without Type Annotations
from typing import Optional


def get_full_name(first_name, last_name):
    return f"{first_name} {last_name}"


# print(get_full_name("john", "smith"))

# With Type Annotations

def get_full_name_with_typing(first_name: str, last_name: str) -> str:
    return f"{first_name.upper()} {last_name.capitalize()}"


print(get_full_name_with_typing("john", "smith"))


def is_eligible(name: str, age: int) -> bool:
    return age >= 18


def complex_operation(first: float, second: bytes) -> float:
    return first


# Union

def process_item(item: int | str):
    print(item)


def say_hello(name: str, welcome: bool | None = None):
    # welcome will be None by default
    if welcome:
        print(f"Hello, {name}")
    else:
        print("Hello")


# Optional

def say_hi(name: Optional[str]):
    print(f"Hey {name}!")


from typing import Annotated


# Type Hints with Metadata Annotations

def greet(name: Annotated[str, "this is just metadata"]) -> str:
    return f"Welcome {name}"
