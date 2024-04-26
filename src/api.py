from datetime import datetime
import uvicorn
from fastapi import Depends, FastAPI, WebSocketDisconnect
from src.auth.models import User
from src.auth.schemas import UserCreate, UserRead, UserUpdate
from src.auth.base_config import auth_backend, fastapi_users
import logging
from fastapi import WebSocket
from fastapi.middleware.cors import CORSMiddleware
from src.celery.tasks import generate_and_save_image
from src.image_generation.connection_manager import wsManager
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


@app.websocket("/generate")
async def websocket_endpoint(websocket: WebSocket, user: User = Depends(get_user_from_cookie)):
    user_id = user.id
    await wsManager.connect(websocket, user_id)
    now = datetime.now()

    try:
        while True:
            data = await websocket.receive_json()
            prompt = data.get("prompt")

            if prompt:
                wsManager.updateConnection(websocket, user_id)
                current_time = now.strftime("%H:%M")
                message = {
                    "time": current_time,
                    "user_id": user_id,
                    "message": f'Received prompt: "{prompt}"',
                    "status": "processing"
                }
                await wsManager.send_personal_message(message=json.dumps(message), user_id=user_id)

                # Call the Celery task and get the AsyncResult object
                result = generate_and_save_image.apply_async(args=[prompt])

                # Wait for the task to complete and get the result
                image_url = await result.get()

                if image_url:
                    # Send the image URL to the frontend
                    message = {
                        "time": current_time,
                        "user_id": user_id,
                        "message": f'Image generated: "{image_url}"',
                        "status": "completed"
                    }
                    await wsManager.send_personal_message(message=json.dumps(message), user_id=user_id)
                else:
                    # Handle the case when image generation fails
                    message = {
                        "time": current_time,
                        "user_id": user_id,
                        "message": "Failed to generate image",
                        "status": "error"
                    }
                    await wsManager.send_personal_message(message=json.dumps(message), user_id=user_id)

    except WebSocketDisconnect:
        wsManager.disconnect(user_id)

host = "0.0.0.0"
port = 8002

if __name__ == '__main__':
    uvicorn.run("src.api:app", host=host, port=port,
                reload=True, log_level="info")
