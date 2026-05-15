from ninja import Schema
from typing import List


class ReviewOut(Schema):
    id: int
    product_id: int
    user: str
    rating: int
    comment: str
    created_at: str


class ReviewIn(Schema):
    user_id: int
    rating: int
    comment: str


class MessageSchema(Schema):
    message: str


class OrderItemOut(Schema):
    product_id: int
    product_name: str
    quantity: int


class OrderOut(Schema):
    id: int
    user: str
    created_at: str
    items: List[OrderItemOut]
