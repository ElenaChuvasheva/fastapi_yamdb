import uvicorn
from fastapi import FastAPI
from sqladmin import Admin
from sqlalchemy import select

from app.admin import CategoryAdmin, GenreAdmin, UserAdmin
from app.models.dbase import database, engine
from app.models.users import User
from app.routers import posts

app = FastAPI()

@app.on_event("startup")
async def startup():
    await database.connect()

@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()

app.include_router(posts.router)

admin = Admin(app, engine)
admin.add_view(CategoryAdmin)
admin.add_view(GenreAdmin)
admin.add_view(UserAdmin)


@app.get("/")
async def read_root():
#    query = (
#        select(
#            [
#                Test.id,
#                Test.name,
#            ]
#        )
#        .select_from(Test)
#    )
    query = select(User)
    return await database.fetch_all(query)


if __name__ == '__main__':
    uvicorn.run(app, host='0.0.0.0', port=8000)
