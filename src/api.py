import uvicorn
from fastapi import FastAPI, Depends
from fastapi.middleware.cors import CORSMiddleware
from src.auth.models import User
from src.auth.schemas import UserCreate, UserRead, UserUpdate
from src.auth.base_config import auth_backend, fastapi_users
from sse_starlette.sse import EventSourceResponse

import asyncio
import json

app = FastAPI(root_path="/api")

origins = [
    "http://localhost:5173",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(
    fastapi_users.get_auth_router(auth_backend),
    prefix="/auth/jwt",
    tags=["auth"]
)
app.include_router(
    fastapi_users.get_register_router(UserRead, UserCreate),
    prefix="/auth",
    tags=["auth"],
)

app.include_router(
    fastapi_users.get_users_router(UserRead, UserUpdate),
    prefix="/users",
    tags=["users"],
)

current_user = fastapi_users.current_user()


async def generate_events(prompt):
    if not prompt:
        yield json.dumps({"status": "error", "error": "Prompt is required"})
        return

    yield {
        "event": "message",
        "id": 1,
        "data": "Uploading"
    }

    try:
        # Placeholder: Simulate a delay
        await asyncio.sleep(3)

        yield {
            "event": "message",
            "id": 2,
            "data": "Image.jpg"
        }
    except Exception as e:
        yield {
            "event": "message",
            "id": 3,
            "data": "Random error message"
        }
        return


@app.get("/generate")
def generate_image(prompt: str, user: User = Depends(current_user)):
    return EventSourceResponse(generate_events(prompt), ping=5)


host = "0.0.0.0"
port = 8002

if __name__ == '__main__':
    uvicorn.run("src.api:app", host=host, port=port,
                reload=True, log_level="info")
