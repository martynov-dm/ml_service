import uvicorn
from fastapi import Depends, FastAPI, WebSocketDisconnect
from src.auth.models import User
from src.auth.schemas import UserCreate, UserRead, UserUpdate
from src.auth.base_config import auth_backend, fastapi_users
import logging
from fastapi import WebSocket
from fastapi.middleware.cors import CORSMiddleware
import datetime
from src.image_generation.connection_manager import manager
from src.utils.get_user_from_cookie import get_user_from_cookie
import json

logger = logging.getLogger(__name__)


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


@app.websocket("/ws/{client_id}")
async def websocket_endpoint(websocket: WebSocket, user: User = Depends(get_user_from_cookie)):
    user_id = user.id
    await manager.connect(websocket, user_id)
    now = datetime.now()
    current_time = now.strftime("%H:%M")
    try:
        while True:
            data = await websocket.receive_text()
            message = {"time": current_time,
                       "user_id": user_id, "message": data}
            await manager.send_personal_message(message=json.dumps(message), user_id=user_id)
    except WebSocketDisconnect:
        manager.disconnect(user_id)
        message = {"time": current_time,
                   "user_id": user_id, "message": "Offline"}
        await manager.broadcast(json.dumps(message))


host = "0.0.0.0"
port = 8002

if __name__ == '__main__':
    uvicorn.run("src.api:app", host=host, port=port,
                reload=True, log_level="info")
