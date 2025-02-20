from fastapi import APIRouter, Depends
from src.core.service.product.product import get_product_service
from src.core.schemas.product.product import (
    ProductAddSchema,
    ProductResponseSchema
)

product_api: APIRouter = APIRouter(prefix="/product", tags=['product'])


@product_api.post('/add/', status_code=200, response_model=ProductResponseSchema)
async def add_product(
    data: ProductAddSchema,
    service=Depends(get_product_service)
):
    return await service.add(**data.dict())
