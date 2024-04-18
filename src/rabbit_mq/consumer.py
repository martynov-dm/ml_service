import pika
import json
from src.services.cloudinary import upload_image
from src.services.hugging_face import generate_image
from connection import connection_params


def callback(ch, method, properties, body):
    message = json.loads(body)
    text = message['text']
    chat_id = message['chat_id']
    print(f"Received message: {text}")

    try:
        # Генерация изображения с помощью ML-сервиса
        image_data = generate_image(text)

        if image_data:
            # Загрузка изображения на хостинг изображений
            image_url = upload_image(image_data)

            if image_url:
                print(f"Image uploaded successfully. URL: {image_url}")

                # Отправка ссылки на изображение в чат Telegram
                chat_id = properties.headers['chat_id']
                # send_message(chat_id, f"Generated image: {image_url}")
            else:
                print("Failed to upload image.")
        else:
            print("Failed to generate image.")

    except Exception as e:
        print(f"Error processing message: {str(e)}")


def consume_messages(exchange, queue_name):
    with pika.BlockingConnection(connection_params) as connection:
        channel = connection.channel()
        channel.exchange_declare(exchange=exchange, exchange_type='fanout')
        channel.queue_declare(queue=queue_name, exclusive=True)
        channel.queue_bind(exchange=exchange, queue=queue_name)
        print(f"Waiting for messages in queue: {queue_name}")
        channel.basic_consume(queue=queue_name, on_message_callback=callback, auto_ack=True)
        channel.start_consuming()
        
        



if __name__ == '__main__':
    consume_messages(exchange='image_generation', queue_name='text_queue')