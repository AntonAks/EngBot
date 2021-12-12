from aiogram import types
from loader import dp
from db_handler import Message, User
from keyboards import main_keyboard
from loader import bot


# COMMAND HANDLERS
@dp.message_handler(commands=['start'])
async def _start_command(message: types.Message):
    user = User()
    user.id = message.from_user.id
    try:
        user.user_name = message.from_user.username
    except Exception:
        user.user_name = None
    user.save()
    await message.answer(f"Приветвствую! Сделайте ваш выбор.", reply_markup=main_keyboard())


@dp.message_handler(commands=['get_users'])
async def _get_users(message: types.Message):
    u = User()
    await message.answer(f"{u.get_all()}")


@dp.message_handler(commands=['del_users'])
async def _get_users(message: types.Message):
    u = User()
    u.drop_all()
    await message.answer(f"Пользователи удалены...")


# CALLBACK HANDLERS
@dp.callback_query_handler(lambda c: c.data in ['words_quiz'])
async def aphorism_command(message: types.Message):
    await bot.send_message(message["message"]["chat"]["id"], "WORD QUIZ STARTED!!!")


@dp.callback_query_handler(lambda c: c.data in ['tenses_quiz'])
async def aphorism_command(message: types.Message):
    await bot.send_message(message["message"]["chat"]["id"], "TENSES QUIZ STARTED!!!")


@dp.callback_query_handler(lambda c: c.data in ['tense_tips'])
async def aphorism_command(message: types.Message):
    await bot.send_message(message["message"]["chat"]["id"], "TENSE TIPS !!!")


@dp.callback_query_handler(lambda c: c.data in ['other_grammar'])
async def aphorism_command(message: types.Message):
    await bot.send_message(message["message"]["chat"]["id"], "OTHER GRAMMAR TIPS !!!")


# COMMON MESSAGE HANDLER
# @dp.message_handler()
# async def echo_message(message: types.Message):
#     m = Message()
#     m.save()
#     await message.answer(f"echo answer: {message['text']}")

