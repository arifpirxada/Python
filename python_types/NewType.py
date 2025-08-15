# NewType
from typing import NewType

UserId = NewType('UserId', int)
ProductId = NewType('ProductId', int)

# Type checker treats these as different types
def get_user(new_user_id: UserId) -> str:
    return f"User {new_user_id}"

def get_product(new_product_id: ProductId) -> str:
    return f"Product {new_product_id}"

# Usage
user_id = UserId(123)
product_id = ProductId(456)

get_user(user_id)     # ✅ OK
# get_user(product_id)  # ❌ Type error - ProductId is not UserId