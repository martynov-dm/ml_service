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

class BalanceUpdateSchema(BaseModel):
    amount: float

class UserBalanceSchema(BaseModel):
    id: int
    user_id: int
    balance: float

    class Config:
        orm_mode = True

class UserResponse(BaseModel):
    username: str
    is_created: bool
    role: UserRole

class CreateUserInput(BaseModel):
    username: str
    password: str

@router.post("/", response_model=UserResponse)
async def create_user(user_data: CreateUserInput, db: Session = Depends(get_db)):
    existing_user = db.query(UserModel).filter(UserModel.username == user_data.username).first()
    if existing_user:
        raise HTTPException(status_code=400, detail="Username already taken")
    
    new_user = UserModel(username=user_data.username, password=user_data.password, role=UserRole.USER)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return UserResponse(username=new_user.username, is_created=True, role=new_user.role)

@router.get("/{user_id}", response_model=UserResponse)
async def get_user(user_id: int, db: Session = Depends(get_db)):
    user = db.query(UserModel).filter(UserModel.id == user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    
    return UserResponse(username=user.username, is_created=True, role=user.role)

@router.post("/users/{user_id}/balance", response_model=UserBalanceSchema)
def update_balance(user_id: int, balance_data: BalanceUpdateSchema, db: Session = Depends(get_db)):
    user_balance = db.query(UserBalanceModel).filter(UserBalanceModel.user_id == user_id).first()
    if not user_balance:
        raise HTTPException(status_code=404, detail="User balance not found")
    
    new_balance = user_balance.balance + balance_data.amount
    if new_balance < 0:
        raise HTTPException(status_code=400, detail="Insufficient balance")
    
    transaction = TransactionModel(user_id=user_id, amount=balance_data.amount)
    db.add(transaction)
    
    user_balance.balance = new_balance
    db.commit()
    db.refresh(user_balance)
    
    return user_balance