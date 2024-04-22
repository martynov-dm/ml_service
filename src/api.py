import uvicorn
from fastapi import FastAPI, Depends
from src.auth.models import User
from src.auth.schemas import UserCreate, UserRead
from src.auth.base_config import auth_backend, fastapi_users

app = FastAPI()

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

current_user = fastapi_users.current_user()

@app.get("/protected-route")
def protected_route(user: User = Depends(current_user)):
    return f"Hello, {user.username}"

@app.get("/unprotected-route")
def unprotected_route():
    return f"Hello, anonym"

host = "0.0.0.0"
port = 8002

if __name__ == '__main__':
    uvicorn.run("src.api:app", host=host, port=port, reload=True, log_level="info")