import aio_pika
from src.rabbit_mq.connection_params import get_connection_params
from src.config import RABBIT_MQ_EXCHANGE_NAME


async def publish_message(message_body):
    connection_params = await get_connection_params()
    connection = await aio_pika.connect_robust(connection_params)
    async with connection:
        channel = await connection.channel()
        exchange = await channel.declare_exchange(RABBIT_MQ_EXCHANGE_NAME, aio_pika.ExchangeType.FANOUT)
        await exchange.publish(
            aio_pika.Message(body=message_body.encode()),
            routing_key=""
        )
        print(f"Sent message: {message_body}")
