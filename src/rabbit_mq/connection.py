import pika

from src.config import RABBITMQ_PASSWORD, RABBITMQ_USERNAME

connection_params = pika.ConnectionParameters(
    host='localhost',  # Замените на адрес вашего RabbitMQ сервера
    port=5672,          # Порт по умолчанию для RabbitMQ
    virtual_host='/',   # Виртуальный хост (обычно '/')
    credentials=pika.PlainCredentials(
        username=RABBITMQ_USERNAME,  # Имя пользователя по умолчанию
        password=RABBITMQ_PASSWORD   # Пароль по умолчанию
    ),
    heartbeat=30,
    blocked_connection_timeout=2
)

