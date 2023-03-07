import databases
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

DATABASE_URL = 'sqlite+aiosqlite:///./sql.db'

engine = create_async_engine(DATABASE_URL, future=True, echo=True)
database = databases.Database(DATABASE_URL)

class Test(Base):
    __tablename__ = 'test'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), unique=True)
