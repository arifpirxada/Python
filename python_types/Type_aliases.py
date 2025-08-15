from typing import TypeVar

# Type Aliases
from typing import TypeAlias, Union

## Ways to Define

### 1. Simple Assignment

UserId = int
UserName = str

### 2. TypeAlias Annotation

UserIdNew: TypeAlias = int
UserNameNew: TypeAlias = str

### 3. Type Statement

type UserId = int
type UserName = str

## Union Types and Type Aliases

# Python approach
Status = Union[str, int, None]
# Or with Python 3.10+ syntax
StatusNew = str | int | None

## Generic Type Aliases

T = TypeVar('T')
K = TypeVar('K')
V = TypeVar('V')

# Generic aliases
ApiResponse = dict[str, T]
Repository = dict[K, list[V]]

# Usage
user_response: ApiResponse[dict] = {"data": {"id": 1, "name": "John"}}
user_repo: Repository[int, str] = {1: ["admin", "user"], 2: ["user"]}