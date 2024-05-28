import cloudinary
import cloudinary.uploader

import cloudinary

from src.celery_worker.celery_logger import celery_logger
from src.config import CLOUDINARY_SECRET, CLOUDINARY_API_KEY

cloudinary.config(
    cloud_name="martynov-dm",
    api_key=CLOUDINARY_API_KEY,
    api_secret=CLOUDINARY_SECRET
)


def upload_image(image_bytes):
    try:
        celery_logger.info("Uploading image to Cloudinary...")

        # Upload the image to Cloudinary
        upload_result = cloudinary.uploader.upload(
            image_bytes,
            folder="generated_images",
            public_id=None,
            overwrite=True,
            resource_type="image"
        )

        # Get the URL of the uploaded image
        image_url = upload_result['url']
        celery_logger.info(f'Image_url: {image_url}')
        return image_url

    except cloudinary.exceptions.Error as e:
        celery_logger.error(f"Error uploading image to Cloudinary: {str(e)}")
        return None

    except Exception as e:
        celery_logger.error(f"Error uploading image to Cloudinary: {str(e)}")
        return None
