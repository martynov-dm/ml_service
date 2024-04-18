import pika
from .connection import connection_params

def publish_message(exchange, routing_key, message):
    with pika.BlockingConnection(connection_params) as connection:
        channel = connection.channel()
        channel.exchange_declare(exchange=exchange, exchange_type='fanout')
        channel.basic_publish(exchange=exchange, routing_key=routing_key, body=message)
        print(f"Sent message: {message}")