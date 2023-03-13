from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Category(Base):
    __tablename__ = 'Category'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), unique=True, nullable=False)
    # повесить проверку на слаг!
    slug = Column(String(100), unique=True, nullable=False)


class Genre(Base):
    __tablename__ = 'Genre'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), unique=True, nullable=False)
    # повесить проверку на слаг!
    slug = Column(String(100), unique=True, nullable=False)
