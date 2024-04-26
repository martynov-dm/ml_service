from tokenize import Token
from typing import Final
import os
from dotenv import load_dotenv
from telegram.ext import CommandHandler, MessageHandler, filters, ContextTypes, Application
from telegram import ReplyKeyboardMarkup, Update
import requests
import json
from src.config import API_URL, TELEGRAM_TOKEN
from src.rabbit_mq.publish_message import publish_message

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    reply_markup = ReplyKeyboardMarkup([
        ['/register', '/login'],
        ['/predict', '/balance'],
        ['/deposit']
    ])
    await update.message.reply_text('Добро пожаловать! Выберите действие:', reply_markup=reply_markup)

async def register(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('Введите имя пользователя:')
    context.user_data['state'] = 'registering'

async def login(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('Введите имя пользователя:')
    context.user_data['state'] = 'logging_in'

async def predict(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('Введите текст для генерации видео:')
    context.user_data['state'] = 'predicting'
    context.user_data['chat_id'] = update.effective_chat.id

async def balance(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.effective_user.id
    response = requests.get(f'{API_URL}/users/{user_id}')
    if response.status_code == 200:
        user_data = response.json()
        balance = user_data['balance']
        await update.message.reply_text(f'Ваш баланс: {balance}')
    else:
        await update.message.reply_text('Не удалось получить баланс.')

async def deposit(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('Введите сумму пополнения:')
    context.user_data['state'] = 'depositing'

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_state = context.user_data.get('state')

    if user_state == 'registering':
        username = update.message.text
        response = requests.post(f'{API_URL}/users', json={'username': username, 'password': 'default_password'})
        if response.status_code == 200:
            await update.message.reply_text('Регистрация успешна!')
        else:
            await update.message.reply_text('Ошибка регистрации.')

    elif user_state == 'logging_in':
        username = update.message.text
        response = requests.post(f'{API_URL}/login', json={'username': username, 'password': 'default_password'})
        if response.status_code == 200:
            await update.message.reply_text('Авторизация успешна!')
        else:
            await update.message.reply_text('Ошибка авторизации.')

    elif user_state == 'predicting':
        text = update.message.text
        chat_id = context.user_data['chat_id']
        message = {
            'text': text,
            'chat_id': chat_id
        }
        publish_message(exchange='image_generation', routing_key='', message=json.dumps(message))
        await update.message.reply_text('Текст отправлен на обработку. Ожидайте результата.')


    elif user_state == 'depositing':
        amount = float(update.message.text)
        user_id = update.effective_user.id
        response = requests.post(f'{API_URL}/users/{user_id}/balance', json={'amount': amount})
        if response.status_code == 200:
            await update.message.reply_text('Баланс успешно пополнен!')
        else:
            await update.message.reply_text('Ошибка пополнения баланса.')

    context.user_data['state'] = None

async def error(update: Update, context: ContextTypes.DEFAULT_TYPE):
    print(f'Update {update} caused error {context.error}')



if __name__ == '__main__':
    print('Starting bot...')
    app = Application.builder().token(TELEGRAM_TOKEN).build()

    app.add_handler(CommandHandler('start', start))
    app.add_handler(CommandHandler('register', register))
    app.add_handler(CommandHandler('login', login))
    app.add_handler(CommandHandler('predict', predict))
    app.add_handler(CommandHandler('balance', balance))
    app.add_handler(CommandHandler('deposit', deposit))

    app.add_handler(MessageHandler(filters.TEXT, handle_message))
    app.add_error_handler(error)

    print('Polling...')
    app.run_polling(poll_interval=3)