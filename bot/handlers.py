from aiogram import types
from loader import dp
from db_handler import Message


# COMMON MESSAGE HANDLER
@dp.message_handler()
async def echo_message(message: types.Message):
    m = Message()
    m.save(message)
    await message.answer(f"echo answer: {message['text']}")
