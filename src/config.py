from dotenv import load_dotenv
import os 

load_dotenv('../.env')

DATABASE_URL = os.getenv("DATABASE_URL")
TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN")
BOT_USERNAME = os.getenv("BOT_USERNAME")
API_URL = os.getenv("API_URL")
HUGGING_FACE_TOKEN = os.getenv("HUGGING_FACE_TOKEN")
CLOUDINARY_SECRET = os.getenv("CLOUDINARY_SECRET")
CLOUDINARY_API_KEY = os.getenv("CLOUDINARY_API_KEY")
RABBITMQ_USERNAME = os.getenv("RABBITMQ_USERNAME")
RABBITMQ_PASSWORD = os.getenv("RABBITMQ_PASSWORD")
SECRET_AUTH = os.getenv("RABBITMQ_PASSWORD")
 
#  DATABASE_URL=postgresql+asyncpg://robot-startml-ro:pheiph0hahj1Vaif@postgres.lab.karpov.courses:6432/startml

# postgresql://ml_service_practise_owner:R9lMaT5gsnkX@ep-shy-hill-a2lo5dqd.eu-central-1.aws.neon.tech/ml_service_practise?sslmode=require