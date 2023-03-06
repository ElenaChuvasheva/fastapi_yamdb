from models.posts import Test, engine
from sqlalchemy.orm import sessionmaker

SessionLocal = sessionmaker(autoflush=False, bind=engine)
db = SessionLocal()
test = Test(name='smth1')
db.add(test)
db.commit()
