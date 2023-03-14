from functools import partial

import databases
from sqlalchemy import Column
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

ReqColumn = partial(Column, nullable=False)


DATABASE_URL = 'sqlite+aiosqlite:///./sql.db'

engine = create_async_engine(DATABASE_URL, future=True, echo=True)
database = databases.Database(DATABASE_URL)
