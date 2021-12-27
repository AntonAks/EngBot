from aiogram import types
from loader import dp
from db_handler import User
from keyboards import main_keyboard


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

