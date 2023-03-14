from functools import partial

from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

ReqColumn = partial(Column, nullable=False)


class Category(Base):
    __tablename__ = 'Category'
    id = Column(Integer, primary_key=True, index=True)
    name = ReqColumn(String(100), unique=True)
    # повесить проверку на слаг, втч в Genre!!
    slug = ReqColumn(String(100), unique=True)


class Genre(Base):
    __tablename__ = 'Genre'
    id = ReqColumn(Integer, primary_key=True, index=True)
    name = ReqColumn(String(100), unique=True)
    # повесить проверку на слаг!
    slug = ReqColumn(String(100), unique=True)
