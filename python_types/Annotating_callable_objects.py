from typing import Callable

# A function that takes an int and returns a string
StringFormatter = Callable[[int], str]

def format_number(num: int) -> str:
    return f"Number: {num}"

def process_with_formatter(value: int, formatter: StringFormatter) -> str:
    return formatter(value)

# Usage
result = process_with_formatter(42, format_number)