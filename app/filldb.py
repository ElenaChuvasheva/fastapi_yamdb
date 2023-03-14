import csv
import os

from models.posts import Category, Genre
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CSV_DIR = os.path.join(BASE_DIR, 'app', 'data')

SYNC_DATABASE_URL = 'sqlite:///../sql.db'
sync_engine = create_engine(SYNC_DATABASE_URL, echo=True)
SessionLocal = sessionmaker(autoflush=False, bind=sync_engine)
db = SessionLocal()

def read_file(filename):
    filepath = os.path.join(CSV_DIR, filename)
    with open(filepath, 'r', encoding='utf-8') as f:
        reader = list(csv.reader(f))
    reader.pop(0)
    print(reader)
    return reader


def create_object(DBClass, row):
    if DBClass == Category or DBClass == Genre:
        kwargs = {'id': int(row[0]), 'name': row[1], 'slug': row[2]}
    db.add(DBClass(**kwargs))

def read_to_DB(filename, DBClass):
    reader = read_file(filename)
    for row in reader:
        create_object(DBClass, row)

read_to_DB('category.csv', Category)
read_to_DB('genre.csv', Genre)

db.commit()
