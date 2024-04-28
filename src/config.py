from dotenv import load_dotenv
import os

load_dotenv('../.env')

SYNC_DATABASE_URL = os.getenv("SYNC_DATABASE_URL")
ASYNC_DATABASE_URL = os.getenv("ASYNC_DATABASE_URL")

TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN")
BOT_USERNAME = os.getenv("BOT_USERNAME")

HUGGING_FACE_TOKEN = os.getenv("HUGGING_FACE_TOKEN")
MODEL_API_URL = os.getenv("MODEL_API_URL")

CLOUDINARY_SECRET = os.getenv("CLOUDINARY_SECRET")
CLOUDINARY_API_KEY = os.getenv("CLOUDINARY_API_KEY")

RABBITMQ_USERNAME = os.getenv("RABBITMQ_USERNAME")
RABBITMQ_PASSWORD = os.getenv("RABBITMQ_PASSWORD")
RABBIT_MQ_EXCHANGE_NAME = os.getenv("RABBIT_MQ_EXCHANGE_NAME")
RABBIT_MQ_QUEUE_NAME = os.getenv("RABBIT_MQ_QUEUE_NAME")

SECRET_AUTH = os.getenv("SECRET_AUTH")
JWT_COOKIE_NAME = os.getenv("JWT_COOKIE_NAME")
API_LOCAL_URL = os.getenv("API_LOCAL_URL")
API_PROD_URL = os.getenv("API_PROD_URL")
