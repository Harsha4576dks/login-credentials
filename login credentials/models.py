from sqlalchemy import Table, String, Column, Integer
from database import metadata

users = Table(
    "users",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("username", String(50), unique=True, nullable=False, index=True),
    Column("password", String)
)