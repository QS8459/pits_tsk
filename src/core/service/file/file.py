from sqlalchemy.ext.asyncio import AsyncSession
from src.core.service.base import BaseService
from src.db.engine import get_async_session
from src.db.models.files import File
from fastapi import Depends


class FileService(BaseService):

    def __init__(self, session: AsyncSession):
        super().__init__(session, File)

    async def before_add(self, *args, **kwargs):
        pass


def get_file_service(session=Depends(get_async_session)) -> FileService:
    return FileService(session)
