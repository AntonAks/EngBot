from aiogram import types
from loader import dp
import keyboards as kb
from tzwhere import tzwhere

@dp.message_handler(content_types=['text'])
async def request_location(message: types.Message):
    await message.answer('Для направления уведомлений нам нужно знать Ваш часовой пояс. \n'
                         'Пожалуйста укажите свою геолокацию.', reply_markup=kb.markup_request_location)

@dp.message_handler(content_types=['location'])
async def handle_loc(message):
    tz = tzwhere.tzwhere()
    timezone = tz.tzNameAt(message.location['latitude'], message.location['longitude'])
    print(timezone)
from db_handler import Message, User


@dp.message_handler(commands=['start'])
async def _start_command(message: types.Message):
    user = User()
    user.id = message.from_user.id
    try:
        user.user_name = message.from_user.username
    except Exception:
        user.user_name = None
    user.save()
    await message.answer(f"Пользователь сохранен! {user}")


@dp.message_handler(commands=['get_users'])
async def _get_users(message: types.Message):
    await message.answer(f"{User.get_all_users()}")


@dp.message_handler(commands=['del_users'])
async def _get_users(message: types.Message):
    User.drop_collection()
    await message.answer(f"Пользователи удалены...")


# COMMON MESSAGE HANDLER
# @dp.message_handler()
# async def echo_message(message: types.Message):
#     await message.answer(f"echo answer: {message['text']}")
@dp.message_handler()
async def echo_message(message: types.Message):
    m = Message()
    m.save()
    await message.answer(f"echo answer: {message['text']}")
