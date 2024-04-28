from fastapi.logger import logger
import pika
import json

from src.image_generation.upload_image import upload_image
from src.image_generation.generate_image import generate_image

from .connection_params import connection_params


def callback(ch, method, properties, body):
    try:
        message = json.loads(body)
        text = message['text']
        chat_id = message['chat_id']
        logger.info(f"Received message: {text}")

        # Генерация изображения с помощью ML-сервиса
        image_bytes = generate_image(text)

        if image_bytes:
            # Загрузка изображения на хостинг изображений
            image_url = upload_image(image_bytes)

            if image_url:
                logger.info(f"Image uploaded successfully. URL: {image_url}")
                message_status = send_message(
                    chat_id, f"Generated image: {image_url}")
                logger.info(f"Message to {chat_id} was sent " + message_status)
            else:
                logger.error("Failed to upload image.")
        else:
            logger.error("Failed to generate image.")

    except json.JSONDecodeError as e:
        logger.error(f"Error decoding JSON: {str(e)}")
    except KeyError as e:
        logger.error(f"Missing key in JSON message: {str(e)}")
    except Exception as e:
        logger.error(f"Error processing message: {str(e)}")


def consume_messages(exchange, queue_name):
    with pika.BlockingConnection(connection_params) as connection:
        channel = connection.channel()
        channel.exchange_declare(exchange=exchange, exchange_type='fanout')
        channel.queue_declare(queue=queue_name, exclusive=True)
        channel.queue_bind(exchange=exchange, queue=queue_name)
        logger.info(f"Waiting for messages in queue: {queue_name}")
        channel.basic_consume(
            queue=queue_name, on_message_callback=callback, auto_ack=True)
        channel.start_consuming()


if __name__ == '__main__':
    consume_messages(exchange='image_generation', queue_name='text_queue')
