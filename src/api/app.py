from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

from ..database.db import SessionLocal
from src.app.api import users

app = FastAPI()

origins = [
    "http://localhost",
    "http://localhost:8080",
    "http://localhost:5173",
    "*"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["DELETE", "GET", "POST", "PUT"],
    allow_headers=["*"],
)


app.include_router(router=users.router, prefix="/users", tags=["users"])
# app.include_router(router=transactions.router, prefix="/transactions", tags=["transactions"])
# app.include_router(router=tasks.router, prefix="/tasks", tags=["tasks"])
