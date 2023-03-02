from models.posts import metadata, test_table
from sqlalchemy import create_engine

engine = create_engine('sqlite:///../sql_app.db', echo=True)

ins = test_table.insert().values(name='test')

conn = engine.connect()
result = conn.execute(ins)

# conn.commit()
