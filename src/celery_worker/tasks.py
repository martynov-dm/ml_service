from celery import Celery
from src.celery_worker.celery_logger import celery_logger
from src.config import RABBITMQ_PASSWORD, RABBITMQ_USERNAME
from src.celery_worker.generate_and_save_image.save_to_db import save_to_db
from src.celery_worker.generate_and_save_image.upload_image import upload_image
from src.celery_worker.generate_and_save_image.generate_image import generate_image


celery_worker = Celery(
    'tasks',
    broker=f'amqp://{RABBITMQ_USERNAME}:{RABBITMQ_PASSWORD}@localhost:5672//'
)
celery_worker.conf.broker_connection_retry_on_startup = True
celery_worker.conf.result_backend = 'rpc://'


@celery_worker.task
def generate_and_save_image(prompt, user_id):

    try:
        generated_image = generate_image(prompt)
        if generated_image is None:
            celery_logger.error("Failed to generate image")
            return None

        image_url = upload_image(generated_image)
        if image_url is None:
            celery_logger.error("Failed to upload image")
            return None

        saved_image = save_to_db(prompt, image_url, user_id)
        if saved_image is None:
            celery_logger.error("Failed to save to db")
            return None

        celery_logger.info(f"Task is finished with {saved_image}")
        return saved_image
    except Exception as e:
        celery_logger.error(f"Error generating and saving image: {e}")
        return None
