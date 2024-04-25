from fastapi.testclient import TestClient
from fastapi_users_db_sqlalchemy import SQLAlchemyUserDatabase
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker
from src.auth.models import User
from src.auth.utils import get_user_db
from src.database import Base
from src.api import app

SQLALCHEMY_DATABASE_URL = "sqlite+aiosqlite://"
async_engine = create_async_engine(
    SQLALCHEMY_DATABASE_URL,
    connect_args={"check_same_thread": False},
)
AsyncTestingSessionLocal = sessionmaker(
    autocommit=False, autoflush=False, bind=async_engine, class_=AsyncSession
)


async def override_get_db():
    db = AsyncTestingSessionLocal()
    try:
        yield SQLAlchemyUserDatabase(db, User)
    finally:
        await db.close()

app.dependency_overrides[get_user_db] = override_get_db

client = TestClient(app)


async def create_tables():
    async with async_engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)


def test_user_api():
    user_credentials = {
        "email": "deadpool@example.com",
        "username": "deadpool@example.com",
        "password": "chimichangas4life"
    }
    import asyncio
    asyncio.run(create_tables())

    response = client.post(
        "/auth/register",
        json=user_credentials,
    )
    assert response.status_code == 201, response.text
    data = response.json()
    assert data["email"] == "deadpool@example.com"
    assert "id" in data
    user_id = data["id"]

    login_credentials = {
        "username": user_credentials["username"],
        "password": user_credentials["password"]
    }

    response = client.post("/auth/jwt/login", data=login_credentials)
    assert response.status_code == 204, response.text
    cookies = response.cookies
    assert "image_prediction_app" in cookies

 # Include the image_prediction_app cookie in the request cookies
    cookies_dict = {"image_prediction_app": cookies["image_prediction_app"]}

    response = client.get("/users/me", cookies=cookies_dict)
    assert response.status_code == 200, response.text
    data = response.json()
    assert data["email"] == user_credentials["email"]
    assert data["id"] == user_id
