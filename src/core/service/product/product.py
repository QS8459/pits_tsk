from src.core.service.base import BaseService
from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession
from src.db.models import Product
from src.db.engine import get_async_session


class ProductService(BaseService):
    def __init__(self, session: AsyncSession):
        super().__init__(session, Product)

    async def before_add(self, **kwargs):
        pass


def get_product_service(session=Depends(get_async_session)) -> ProductService:
    return ProductService(session)
