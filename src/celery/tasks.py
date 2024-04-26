from celery import Celery
from src.config import RABBITMQ_PASSWORD, RABBITMQ_USERNAME
from src.image_generation import upload_image
from src.image_generation.generate_image import generate_image
from src.image_generation.models import Image

celery = Celery(
    'tasks', broker=f'amqp://{RABBITMQ_USERNAME}:{RABBITMQ_PASSWORD}@localhost:5672//')

celery.conf.broker_connection_retry_on_startup = True
celery.conf.result_backend = 'rpc://'


@celery.task
def generate_and_save_image(prompt):
    try:
        generated_image = generate_image(prompt)
        if generated_image is None:
            raise Exception("Failed to generate image")

        image_url = upload_image(generated_image)

        image = Image(prompt=prompt, url=image_url)
        image.save()

        return image_url  # Return the image URL

    except Exception as e:
        print(f"Error generating and saving image: {str(e)}")
        return None  # Return None in case of an error


# @celery.task
# def distribute_image(image_id):
#     try:
#         # Retrieve the image from the database
#         image = Image.objects.get(id=image_id)

#         # Send the image to the frontend
#         send_image_to_frontend(image.url)

#         # Send the image to the Telegram client
#         send_image_to_telegram(image.url)

#     except Image.DoesNotExist:
#         print(f"Image with ID {image_id} not found")
#     except Exception as e:
#         print(f"Error distributing image: {str(e)}")


# def send_image_to_frontend(image_url):
#     # Logic to send the image URL to the frontend
#     # You can use WebSocket, server-sent events, or any other mechanism
#     pass
