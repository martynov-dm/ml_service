import requests

from src.config import TELEGRAM_TOKEN


def send_message(chat_id, text):
    message = "hello from your telegram bot"
    url = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage?chat_id={chat_id}&text={text}"
    return requests.get(url).json()