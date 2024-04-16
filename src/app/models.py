from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, Float, func
from sqlalchemy.orm import relationship, backref
from src.app.db import Base, engine

class UserModel(Base):
    __tablename__ = 'users_d-martynov-1_practicum'
    __table_args__ = {"schema": "public", 'extend_existing': True}

    id = Column(Integer, primary_key=True)
    username = Column(String(50), unique=True, nullable=False)
    password = Column(String(255), nullable=False)
    role = Column(String(20), default='user')

    transactions = relationship('TransactionModel', back_populates='user')
    tasks = relationship('TaskModel', back_populates='user')
    balance = relationship('UserBalanceModel', uselist=False, back_populates='user')


class TransactionModel(Base):
    __tablename__ = 'transactions_d-martynov-1_practicum'
    __table_args__ = {"schema": "public", 'extend_existing': True}


    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users_d-martynov-1_practicum.id'), nullable=False)
    amount = Column(Float, nullable=False)
    timestamp = Column(DateTime, nullable=False, default=func.now())

    user = relationship('UserModel', back_populates='transactions')

class TaskModel(Base):
    __tablename__ = 'tasks_d-martynov-1_practicum'
    __table_args__ = {"schema": "public", 'extend_existing': True}

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users_d-martynov-1_practicum.id'), nullable=False)
    model_name = Column(String, nullable=False)
    input_data = Column(String, nullable=False)
    status = Column(String, nullable=False)
    result = Column(String, nullable=True)
    created_at = Column(DateTime, nullable=False, default=func.now())
    updated_at = Column(DateTime, nullable=False, default=func.now(), onupdate=func.now())

    user = relationship('UserModel', back_populates='tasks')

class UserBalanceModel(Base):
    __tablename__ = 'user_balances'
    __table_args__ = {"schema": "public", 'extend_existing': True}

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users_d-martynov-1_practicum.id'), unique=True, nullable=False)
    balance = Column(Float, nullable=False, default=10.0)

    user = relationship('UserModel', back_populates='balance')


Base.metadata.create_all(bind=engine)

