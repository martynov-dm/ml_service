from collections import defaultdict
from typing import DefaultDict, Optional
from fastapi import WebSocket, WebSocketDisconnect
from fastapi.logger import logger

class ConnectionManager:
    def __init__(self):
        self.active_connections: DefaultDict[int, Optional[WebSocket]] = defaultdict(
            lambda: None)

    async def connect(self, websocket: WebSocket, user_id: int):
        try:
            await websocket.accept()
            self.active_connections[user_id] = websocket
            logger.info(
                f"New WebSocket connection established for user_id {user_id}")
        except Exception as e:
            logger.error(f"Error accepting WebSocket connection for user_id {
                         user_id}: {e}")

    def disconnect(self, user_id: int):
        if user_id in self.active_connections:
            self.active_connections.pop(user_id)
            logger.info(f"WebSocket connection closed for user_id {user_id}")

    async def send_personal_message(self, message: str, user_id: int):
        if user_id in self.active_connections and self.active_connections[user_id] is not None:
            websocket = self.active_connections[user_id]
            try:
                await websocket.send_text(message)
                logger.info(f"Sent message to user_id {user_id}: {message}")
            except WebSocketDisconnect:
                logger.warning(f"WebSocket disconnected for user_id {user_id}")
                self.disconnect(user_id)
            except Exception as e:
                logger.error(f"Error sending message to user_id {
                             user_id}: {e}")
        else:
            logger.warning(
                f"No active WebSocket connection found for user_id {user_id}")


wsManager = ConnectionManager()
