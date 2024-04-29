from contextlib import contextmanager
from typing import AsyncGenerator

from src.config import ASYNC_DATABASE_URL, SYNC_DATABASE_URL

from sqlalchemy import MetaData, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, scoped_session
from sqlalchemy.pool import NullPool

from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from src.fastapi_logger import fastapi_logger

Base = declarative_base()
metadata = MetaData()

async_engine = create_async_engine(ASYNC_DATABASE_URL, poolclass=NullPool,)
sync_engine = create_engine(
    SYNC_DATABASE_URL
)

async_session_maker = sessionmaker(
    async_engine, class_=AsyncSession, expire_on_commit=False)
sync_session_maker = sessionmaker(
    autocommit=False, autoflush=False, bind=sync_engine)


async def get_async_session() -> AsyncGenerator[AsyncSession, None]:
    async with async_session_maker() as session:
        yield session


@contextmanager
def get_sync_session():
    session = scoped_session(sync_session_maker)()
    try:
        yield session
    finally:
        try:
            session.close()
        except Exception as e:
            fastapi_logger.error(f"Error closing database session: {e}")
