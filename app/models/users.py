from sqlalchemy import Column, Integer, String, Text

from app.models.dbase import Base, ReqColumn


class User(Base):
    __tablename__ = 'User'
    id = Column(Integer, primary_key=True, index=True)
    username = ReqColumn(String(100), unique=True)
    email = ReqColumn(String(100), unique=True)
    first_name = Column(String(100))
    last_name = Column(String(100))
    bio = Column(Text())
    # какой валидатор вешать на роль? там был choice
    role = ReqColumn(String(100))
