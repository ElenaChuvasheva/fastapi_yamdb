from sqladmin import ModelView

from app.models.posts import Category, Genre
from app.models.users import User


class CategoryAdmin(ModelView, model=Category):
    column_list = [Category.id, Category.name, Category.slug]


class GenreAdmin(ModelView, model=Genre):
    column_list = [Genre.id, Genre.name, Genre.slug]


class UserAdmin(ModelView, model=User):
    column_list = [User.id, User.username, User.email, User.role]
