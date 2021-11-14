from aiogram import Bot, Dispatcher, types
import settings

bot = Bot(token=settings.API_TOKEN, parse_mode=types.ParseMode.HTML)
dp = Dispatcher(bot)
