import aio_pika
from src.config import RABBITMQ_PASSWORD, RABBITMQ_USERNAME

async def get_connection_params():
    # Create a secure connection parameters instance
    connection_params = aio_pika.ConnectionParameters(
        host='localhost',  # Replace with your RabbitMQ server address
        port=5672,  # Default RabbitMQ port
        virtualhost='/',  # Virtual host (usually '/')
        credentials=aio_pika.PlainCredentials(
            username=RABBITMQ_USERNAME,  # Default username
            password=RABBITMQ_PASSWORD  # Default password
        ),
        heartbeat=30,  # Heartbeat interval (in seconds)
        blocked_connection_timeout=2  # Timeout for blocked connections
    )
    return connection_params