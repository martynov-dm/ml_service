from fastapi import WebSocket
from src.api import logger


async def image_generation_websocket(websocket: WebSocket, prompt: str, user_id: str):
    await websocket.accept()
    try:
        await websocket.send_text("Processing prompt")
        # task_id = await submit_prompt(prompt, "websocket", user_id)
        # result = await get_task_result(task_id)
        # await websocket.send_text(f"Image URL: tesr.jpg")
    except Exception as e:
        logger.exception("Error processing prompt")
        await websocket.send_text("Error processing prompt")
    finally:
        await websocket.close()
