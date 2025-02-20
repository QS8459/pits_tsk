from abc import ABC, abstractmethod
from typing import Generic, TypeVar, Type, Callable
from fastapi.exceptions import HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.exc import SQLAlchemyError, IntegrityError
from src.conf.log import log
from sqlalchemy.future import select
from uuid import UUID


T = TypeVar("T")


class BaseService(ABC, Generic[T]):

    def __init__(self, session: AsyncSession, model: Type[T]):
        self.session = session
        self.model = model
        self.instance = None

    async def __handle_in_session(self, _call: Callable, refresh=False, *args, **kwargs):
        try:
            result = await _call(*args, **kwargs)
            await self.session.commit()
            if refresh:
                await self.session.refresh(result)
            return result
        except SQLAlchemyError as e:
            log.error(f"Exception Happened while handling Session\n{e}")
            await self.session.rollback()
            raise HTTPException(
                status_code=500,
                detail={
                    'detail': "Something went wrong"
                }
            )

    async def exec_in_session(self, _call: Callable, refresh=False, fetch_one=False, update=False, *args, **kwargs):
        if refresh:
            return await self.__handle_in_session(_call, refresh=True, *args, **kwargs)
        if update:
            return await self.__handle_in_session(_call, refresh=False, *args, **kwargs)
        result = await self.__handle_in_session(_call, *args, **kwargs)
        if fetch_one:
            return result.scalars().first()

        return result.scalars().all()

    @abstractmethod
    async def before_add(self, **kwargs):
        pass

    async def add(self, *args, **kwargs):
        async def _add(*in_args, **in_kwargs):
            self.instance = self.model(**in_kwargs)
            await self.before_add(**in_kwargs)
            self.session.add(self.instance)
            return self.instance

        result = await self.exec_in_session(_add, refresh=True, *args, **kwargs)
        return result

    async def get_by_id(self, uid: UUID):
        async def _get_by_id(in_uid: UUID):
            instance = self.model
            query = select(instance).where(self.model.uid == in_uid)
            return await self.session.execute(query)

        result = await self.exec_in_session(_get_by_id, in_uid=uid, fetch_one=True)
        if not result:
            raise HTTPException(400, "No instance found")
        return result

    async def update(self, uid: UUID, *args, **kwargs):
        async def _update(in_uid: UUID, *in_args, **in_kwargs):
            instance = await self.get_by_id(uid=in_uid)
            for key, value in in_kwargs.items():
                log.info(f"This is the value I got {value}")
                log.info(f"This is the key {key}")
                setattr(instance, key, value)
            return instance

        await self.exec_in_session(_update, update=True, in_uid=uid, *args, **kwargs)
        after_commit = await self.get_by_id(uid=uid)
        return after_commit

    async def h_delete(self, uid):
        async def _h_delete(in_uid):
            instance = await self.get_by_id(uid=in_uid)
            return await self.session.delete(instance)

        return await self.exec_in_session(_h_delete, in_uid=uid, update=True)
