from sqlalchemy import create_engine, MetaData
from databases import Database

DATABASE_URL = "postgresql://postgres:jag88@localhost:5432/Login"

database = Database(DATABASE_URL)
metadata = MetaData()
engine = create_engine(DATABASE_URL)