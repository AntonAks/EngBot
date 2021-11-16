from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

markup_request = ReplyKeyboardMarkup(resize_keyboard=True).add(KeyboardButton('Отправить свою геолокацию', request_location=True))