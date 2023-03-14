from models.posts import Category
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

SYNC_DATABASE_URL = 'sqlite:///../sql.db'
sync_engine = create_engine(SYNC_DATABASE_URL, echo=True)
SessionLocal = sessionmaker(autoflush=False, bind=sync_engine)
db = SessionLocal()
test = Category(name='smth3', slug='slug2')
db.add(test)
db.commit()
