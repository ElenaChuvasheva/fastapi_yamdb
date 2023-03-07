import uvicorn
from fastapi import FastAPI
from sqladmin import Admin, ModelView
from sqlalchemy import select

from app.models.posts import Test, database, engine
from app.routers import posts

app = FastAPI()

@app.on_event("startup")
async def startup():
    await database.connect()

@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()

app.include_router(posts.router)

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
    query = select(Test)
    return await database.fetch_all(query)

admin = Admin(app, engine)

class TestAdmin(ModelView, model=Test):
    column_list = [Test.id, Test.name]


admin.add_view(TestAdmin)

if __name__ == '__main__':
    uvicorn.run(app, host='0.0.0.0', port=8000)