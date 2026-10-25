from typing import List
from pydantic import BaseModel

# 4. Create schemas

# Article inside UserDisplay
class Article(BaseModel):
    title: str
    content: str
    published: bool
    class Config():
        orm_mode = True

# The data that comes from the user
class UserBase(BaseModel):
    username: str
    email: str
    password: str

# What we show to our users
class UserDisplay(BaseModel):
    username: str
    email: str
    items: List[Article] = []
    class Config():
        orm_mode = True # Allows the system to return database data in the above format

class ArticleBase(BaseModel):
    title: str
    content: str
    published: bool
    creator_id: int

# User inside ArticleDisplay
class User(BaseModel):
    id: int
    username: str
    class Config():
        orm_mode = True

class ArticleDisplay(BaseModel):
    title: str
    content: str
    published: bool
    user: User
    class Config():
        orm_mode = True
