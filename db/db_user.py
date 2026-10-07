from fastapi import HTTPException, status
from db.hash import Hash
from sqlalchemy.orm.session import Session
from schemas import UserBase
from db.models import DBUser

# 3. Create functionality to write to database

def create_user(db: Session, request: UserBase):
    new_user = DBUser(
        username = request.username,
        email = request.email,
        password = Hash.bcrypt(request.password)
    )

    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

def get_all_users(db: Session):
    return db.query(DBUser).all()

def get_user(db: Session, id: int):
    return db.query(DBUser).filter(DBUser.id == id).first()

def update_user(db: Session, id: int, request: UserBase):
    user = db.query(DBUser).filter(DBUser.id == id)
    user.update({
        DBUser.username: request.username,
        DBUser.email: request.email,
        DBUser.password: Hash.bcrypt(request.password)
    })

    db.commit()
    return 'OK'

def delete_user(db: Session, id: int):
    # 1. Fetch the user
    user = db.query(DBUser).filter(DBUser.id == id).first()
    
    # 2. Check if the user exists to prevent crashes
    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"User with id {id} not found"
        )

    # 3. Stage the deletion
    db.delete(user)
    
    # 4. Permanently commit the transaction to the database
    db.commit()
    
    return f"User with id {id} successfully deleted"
    