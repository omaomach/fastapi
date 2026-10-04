from sqlalchemy.orm.session import Session
from schemas import UserBase
from db.models import DBUser

def createUser(db: Session, request: UserBase):
    new_user = DBUser(
        username = request.username,
        email = request.email,
        password = 
    )