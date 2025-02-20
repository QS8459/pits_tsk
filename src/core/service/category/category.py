from src.core.service.base import BaseService
from src.db.engine import get_async_session
from src.db.models.category import Category
from sqlalchemy.ext.asyncio import AsyncSession
from fastapi import Depends


class CategoryService(BaseService):

    def __init__(self, session: AsyncSession):
        super().__init__(session, Category)

    async def before_add(self):
        pass


def get_category_service(session=Depends(get_async_session)) -> CategoryService:
    return CategoryService(session)
