
from fastapi_users_db_sqlalchemy import SQLAlchemyBaseUserTable
from sqlalchemy import Column, Integer, String, Boolean

from database import Base


# user = Table(
#     "user_d-martynov-1_ml_service",
#     metadata,
#     Column("id", Integer, primary_key=True),
#     Column("email", String, nullable=False),
#     Column("username", String, nullable=False),
#     Column("hashed_password", String, nullable=False),
#     Column("is_active", Boolean, default=True, nullable=False),
#     Column("is_superuser", Boolean, default=False, nullable=False),
#     Column("is_verified", Boolean, default=False, nullable=False),
# )

class User(SQLAlchemyBaseUserTable[int], Base):
    id = Column(Integer, primary_key=True)
    email = Column(String, nullable=False)
    username = Column(String, nullable=False)
    hashed_password: str = Column(String(length=1024), nullable=False)
    is_active: bool = Column(Boolean, default=True, nullable=False)
    is_superuser: bool = Column(Boolean, default=False, nullable=False)
    is_verified: bool = Column(Boolean, default=False, nullable=False)


# class UserModel(Base):
#     __tablename__ = 'users_d-martynov-1_practicum'
#     __table_args__ = {"schema": "public", 'extend_existing': True}
#     id = Column(Integer, primary_key=True)
#     username = Column(String(50), unique=True, nullable=False)
#     password = Column(String(255), nullable=False)
#     role = Column(String(20), default='user')
#     transactions = relationship('TransactionModel', back_populates='user')
#     tasks = relationship('TaskModel', back_populates='user')
#     balance = relationship('UserBalanceModel', uselist=False, back_populates='user')