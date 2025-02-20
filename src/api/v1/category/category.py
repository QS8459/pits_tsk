from fastapi import APIRouter, Depends, status
from src.core.service.category.category import get_category_service
from src.core.schemas.category.category import (
    CategoryAddUpdateSchema,
    CategoryResponseSchema
)

category_api: APIRouter = APIRouter(prefix='/category', tags=['category'])


@category_api.post('/add/', status_code=status.HTTP_201_CREATED, response_model=CategoryResponseSchema)
async def add_category(
        data: CategoryAddUpdateSchema,
        service=Depends(get_category_service)
):
    return await service.add(**data.dict())


@category_api.put("/update/", status_code=status.HTTP_200_OK, response_model=CategoryResponseSchema)
async def update_category(
        uid: str,
        data: CategoryAddUpdateSchema,
        service=Depends(get_category_service)
):
    return await service.update(uid=uid, **data.dict())


@category_api.get('/{pk}/', status_code=status.HTTP_200_OK, response_model=CategoryResponseSchema)
async def category_item(
        uid: str,
        service=Depends(get_category_service)
):
    return await service.get_by_id(uid=uid)


@category_api.delete('/delete/{pk}/', status_code=status.HTTP_202_ACCEPTED)
async def delete_category_item(
        uid: str,
        service=Depends(get_category_service)
):
    result = await service.h_delete(uid=uid)
    return {
        'detail': f"Successfully deleted {result}"
    }
