import asyncio
from typing import Annotated

from sqlalchemy import String, create_engine
from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker, create_async_engine
from sqlalchemy.orm import DeclarativeBase, Session, sessionmaker

from config import settings

postgres_sync_engine = create_engine(
    url=settings.POSTGRES_URL_psycopg,
    echo=True,
    # pool_size=5,
    # max_overflow=10,
)

postgres_async_engine = create_async_engine(
    url=settings.POSTGRES_URL_asyncpg,
    echo=True,
)

session_factory = sessionmaker(postgres_sync_engine)
async_session_factory = async_sessionmaker(postgres_async_engine)
