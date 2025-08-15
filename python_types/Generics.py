from typing import TypeVar

T = TypeVar('T')

def first_item(items: list[T]) -> T:
    return items[0]

# Usage - type is inferred
numbers = first_item([1, 2, 3])      # T is int
names = first_item(["Alice", "Bob"])  # T is str