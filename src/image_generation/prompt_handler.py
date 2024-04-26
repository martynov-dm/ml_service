from src.rabbit_mq.publish_message import publish_message
from .schemas import PromptMessage
from celery.result import AsyncResult


async def submit_prompt(prompt, client_source, user_id):
    message = PromptMessage(
        prompt=prompt, client_source=client_source, user_id=user_id)
    await publish_message(message.model_dump_json())
    return task.id


async def get_task_result(task_id):
    task_result = AsyncResult(task_id)
    result = task_result.get()
    return result
