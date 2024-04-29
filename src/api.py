from datetime import datetime
from multiprocessing.pool import AsyncResult
from typing import Optional
import uvicorn
from fastapi import Depends, FastAPI, WebSocketDisconnect
from src.auth.models import User
from src.auth.schemas import UserCreate, UserRead, UserUpdate
from src.auth.base_config import auth_backend, fastapi_users
from fastapi import WebSocket
from fastapi.middleware.cors import CORSMiddleware
from src.celery.tasks import generate_and_save_image
from src.image_generation.connection_manager import wsManager
from src.image_generation.schemas import ImageInfo
from src.utils.get_user_from_cookie import get_user_from_cookie
import json
from src.fastapi_logger import fastapi_logger


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


# WebSocket endpoint
@app.websocket("/generate")
async def websocket_endpoint(websocket: WebSocket, user: User = Depends(get_user_from_cookie)):
    user_id = user.id
    await wsManager.connect(websocket, user_id)
    try:
        while True:
            data = await websocket.receive_json()
            prompt = data.get("prompt")
            if prompt:
                current_time = datetime.now().strftime("%H:%M")
                message = {
                    "time": current_time,
                    "message": f'Received prompt: "{prompt}"',
                    "status": "processing"
                }
                wsManager.add_connection(websocket, user_id)
                await wsManager.send_personal_message(json.dumps(message), user_id)
                fastapi_logger.info(f'Started task for prompt: {prompt}')

                result: Optional[AsyncResult] = generate_and_save_image.apply_async(
                    args=[prompt, user_id])
                # Wait for the task to complete and get the result
                saved_image: ImageInfo = result.get()
                fastapi_logger.info(
                    f'Image returned from worker: {saved_image}')

                if saved_image is None:
                    # Handle the case when image generation fails
                    message = {
                        "time": current_time,
                        "user_id": user_id,
                        "message": "Failed to generate image",
                        "status": "Error"
                    }
                    await wsManager.send_personal_message(json.dumps(message), user_id)
                else:
                    # Send the image URL to the frontend
                    message = {
                        "time": current_time,
                        "message": saved_image,
                        "status": "Completed"
                    }
                    await wsManager.send_personal_message(json.dumps(message), user_id)
    except WebSocketDisconnect:
        fastapi_logger.info(f"WebSocket disconnected for user_id {user_id}")
        wsManager.disconnect(user_id)
    except Exception as e:
        fastapi_logger.error(
            f"Error in websocket_endpoint for user_id {user_id}: {e}")
        wsManager.disconnect(user_id)

host = "0.0.0.0"
port = 8002

if __name__ == '__main__':
    uvicorn.run("src.api:app", host=host, port=port,
                reload=True, log_level="info")
