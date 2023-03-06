import uvicorn
from fastapi import FastAPI
from sqladmin import Admin, ModelView

from app.models.posts import Test, engine
from app.routers import posts

app = FastAPI()

app.include_router(posts.router)

admin = Admin(app, engine)

class TestAdmin(ModelView, model=Test):
    column_list = [Test.id, Test.name]


admin.add_view(TestAdmin)

if __name__ == '__main__':
    uvicorn.run(app, host='0.0.0.0', port=8000)