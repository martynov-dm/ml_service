import pika

connection_params = pika.ConnectionParameters(
    host='localhost',  # Замените на адрес вашего RabbitMQ сервера
    port=5672,          # Порт по умолчанию для RabbitMQ
    virtual_host='/',   # Виртуальный хост (обычно '/')
    credentials=pika.PlainCredentials(
        username='rmquser',  # Имя пользователя по умолчанию
        password='rmqpassword'   # Пароль по умолчанию
    ),
    heartbeat=30,
    blocked_connection_timeout=2
)

