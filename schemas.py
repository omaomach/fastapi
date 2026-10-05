from pydantic import BaseModel

# The data that comes from the user
class UserBase(BaseModel):
    username: str
    email: str
    password: str

# What we show to our users
class UserDisplay(BaseModel):
    username: str
    email: str
    class Config():
        orm_mode = True # Allows the system to return database data in the above format
