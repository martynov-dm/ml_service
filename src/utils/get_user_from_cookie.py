from fastapi import Depends, WebSocket, WebSocketException

from src.auth.manager import get_user_manager
from src.auth.base_config import auth_backend

from src.config import JWT_COOKIE_NAME


async def get_user_from_cookie(websocket: WebSocket, user_manager=Depends(get_user_manager)):
    cookie = websocket.cookies.get(JWT_COOKIE_NAME)
    user = await auth_backend.get_strategy().read_token(cookie, user_manager)
    if not user or not user.is_active:
        raise WebSocketException("Invalid user")
    yield user
