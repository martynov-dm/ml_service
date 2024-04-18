


TOKEN = '7026890071:AAE0LiI5b0gOdVnYs6ZBcgvQ0H02eGzpZW0'
chat_id = '1218586557'



import requests

message = "hello from your telegram bot"
url = f"https://api.telegram.org/bot{TOKEN}/sendMessage?chat_id={chat_id}&text={message}"
print(requests.get(url).json()) # this sends the message