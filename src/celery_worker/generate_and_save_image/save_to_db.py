from src.celery_worker.celery_logger import celery_logger
from src.database import get_sync_session
from src.image_generation.models import Image
from src.image_generation.schemas import ImageInfo


def save_to_db(prompt, image_url, user_id):
    with get_sync_session() as session:
        try:
            image = Image(prompt=prompt, url=image_url, user_id=user_id)
            session.add(image)
            session.commit()
            session.refresh(image)
            image_info = ImageInfo.model_validate(image)
            celery_logger.info(f'Added Image to DB: {
                               image_info.model_dump_json()}')
            return image_info.model_dump()
        except Exception as e:
            celery_logger.error(f"Error saving image to database: {e}")
            return None
