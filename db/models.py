from sqlalchemy.sql.sqltypes import Integer, String
from db.database import Base
from sqlalchemy import Column

# What goes into the database i.e create database models (tables)

class DBUser(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String)
    email = Column(String)
    password = Column(String)

