from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

engine = create_async_engine('sqlite+aiosqlite:///./sql.db', echo=True)

class Test(Base):
    __tablename__ = 'test'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), unique=True)
