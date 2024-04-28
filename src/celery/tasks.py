from celery import Celery
from fastapi.logger import logger
from src.config import RABBITMQ_PASSWORD, RABBITMQ_USERNAME
from src.image_generation.upload_image import upload_image
from src.image_generation.generate_image import generate_image
from src.image_generation.models import Image
from src.database import get_sync_session

celery = Celery(
    'tasks',
    broker=f'amqp://{RABBITMQ_USERNAME}:{RABBITMQ_PASSWORD}@localhost:5672//'
)
celery.conf.broker_connection_retry_on_startup = True
celery.conf.result_backend = 'rpc://'


@celery.task
def generate_and_save_image(prompt, user_id):
    try:
        generated_image = generate_image(prompt)
        if generated_image is None:
            logger.error("Failed to generate image")
            return None

        try:
            image_url = upload_image(generated_image)
        except Exception as e:
            logger.error(f"Error uploading image: {e}")
            return None

        with get_sync_session() as session:
            try:
                image = Image(prompt=prompt, url=image_url, user_id=user_id)
                session.add(image)
                session.commit()
                session.refresh(image)
                logger.info('Added Image to DB', image)
                return image_url
            except Exception as e:
                logger.error(f"Error saving image to database: {e}")
                return None
    except Exception as e:
        logger.error(f"Error generating and saving image: {e}")
        return None
