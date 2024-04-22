
from fastapi_users import schemas


class UserRead(schemas.BaseUser[int]):
    id: int
    email: str
    username: str
    is_active: bool = True
    is_superuser: bool = False
    is_verified: bool = False

    class Config:
        orm_mode = True


class UserCreate(schemas.BaseUserCreate):
    username: str
    email: str
    password: str



# class UserRole(str, Enum):
#     USER = 'user'
#     ADMIN = 'admin'

# class BalanceUpdateSchema(BaseModel):
#     amount: float

# class UserBalanceSchema(BaseModel):
#     id: int
#     user_id: int
#     balance: float

#     class Config:
#         orm_mode = True

# class UserResponse(BaseModel):
#     username: str
#     is_created: bool
#     role: UserRole

# class CreateUserInput(BaseModel):
#     username: str
#     password: str
