from dotenv import load_dotenv
import os 

load_dotenv('../.env')

DATABASE_URL = os.getenv("DATABASE_URL")
TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN")
BOT_USERNAME = os.getenv("BOT_USERNAME")
API_URL = os.getenv("API_URL")
HUGGING_FACE_TOKEN = os.getenv("HUGGING_FACE_TOKEN")
CLOUDINARY_SECRET = os.getenv("CLOUDINARY_SECRET")
