import databases
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine

DATABASE_URL = 'sqlite+aiosqlite:///./sql.db'

engine = create_async_engine(DATABASE_URL, future=True, echo=True)
database = databases.Database(DATABASE_URL)
