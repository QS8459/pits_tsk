from src.db.models.account import Account
from src.core.service.base import BaseService
from src.db.engine import get_async_session
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from fastapi import Depends, HTTPException, status


class AccountService(BaseService):

    def __init__(self, session: AsyncSession):
        super().__init__(session=session, model=Account)

    async def before_add(self, **kwargs):
        password = kwargs.pop('password')
        self.instance.hash_passwd(password=password)
        return 0

    async def get_by_email(self, email: str):
        async def _get_by_email(in_email: str):
            query = select(self.model).where(self.model.email == in_email)
            return await self.session.execute(query)
        user = await self.exec_in_session(_get_by_email, fetch_one=True, in_email=email)
        if not user:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="User Not Found"
            )
        return user

    async def verify_user(self, *args, **kwargs):

        user = await self.get_by_email(email=kwargs.get('email'))

        if user is None:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Wrong Email or password"
            )

        password = user.verify_passwd(password=kwargs.get('password'))

        if password:
            return user
        else:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Wrong Email or password"
            )


def get_account_service(session=Depends(get_async_session)) -> AccountService:
    return AccountService(session)