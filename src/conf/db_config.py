from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine, AsyncEngine, async_sessionmaker
from src.conf.settings import settings

engine: AsyncEngine = create_async_engine(str(settings.PG_URI))
async_session_maker: async_sessionmaker = async_sessionmaker(engine, expire_on_commit=False)