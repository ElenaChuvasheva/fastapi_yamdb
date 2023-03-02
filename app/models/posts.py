import sqlalchemy

metadata = sqlalchemy.MetaData()

test_table = sqlalchemy.Table(
    'test',
    metadata,
    sqlalchemy.Column('id', sqlalchemy.Integer, primary_key=True),
    sqlalchemy.Column('name', sqlalchemy.String(100), unique=True),
)
