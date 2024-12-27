from pydantic import BaseModel
from typing import Optional

class CategoryRequest(BaseModel):
    name: str

class ProductRequest(BaseModel):
    name: str
    price: float
    quantity: int
    category_id: int
