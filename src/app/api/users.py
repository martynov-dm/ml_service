from enum import Enum
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from pydantic import BaseModel

from app.models import UserModel, UserBalanceModel, TransactionModel
from src.app.db import get_db

router = APIRouter()

class UserRole(str, Enum):
    USER = 'user'
    ADMIN = 'admin'

class UserCreateSchema(BaseModel):
    username: str
    password: str
    role: UserRole = UserRole.USER

class BalanceUpdateSchema(BaseModel):
    diff_amount: float

class UserBalanceSchema(BaseModel):
    id: int
    user_id: int
    balance: float

    class Config:
        orm_mode = True

@router.post("/", response_model=UserModel)
async def create_user(user: UserCreateSchema, db: Session = Depends(get_db)):
    existing_user = db.query(UserModel).filter(UserModel.username == user.username).first()
    if existing_user:
        raise HTTPException(status_code=400, detail="Username already taken")
    new_user = UserModel(username=user.username, password=user.password, role=user.role)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

@router.get("/{user_id}", response_model=UserModel)
async def get_user(user_id: int, db: Session = Depends(get_db)):
    db_user = db.query(UserModel).filter(UserModel.id == user_id).first()
    if not db_user:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user

@router.post("/users/{user_id}/balance", response_model=UserBalanceSchema)
def update_balance(user_id: int, balance_update: BalanceUpdateSchema, db: Session = Depends(get_db)):
    user_balance = db.query(UserBalanceModel).filter(UserBalanceModel.user_id == user_id).first()
    if not user_balance:
        raise HTTPException(status_code=404, detail="User not found")
    new_balance = user_balance.balance + balance_update.diff_amount
    if new_balance < 0:
        raise HTTPException(status_code=400, detail="Insufficient balance")
    transaction = TransactionModel(user_id=user_id, amount=balance_update.diff_amount)
    db.add(transaction)
    user_balance.balance = new_balance
    db.commit()
    db.refresh(user_balance)
    return user_balance