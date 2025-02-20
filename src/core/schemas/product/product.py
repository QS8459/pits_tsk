from pydantic import BaseModel
from uuid import UUID


class ProductBaseSchema(BaseModel):
    name: str
    quantity: int
    price: float


class ProductAddSchema(ProductBaseSchema):
    pass


class ProductResponseSchema(ProductBaseSchema):
    uid: UUID