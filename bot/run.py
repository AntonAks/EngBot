from loader import bot


async def on_shutdown(dp):
    await bot.close()


async def on_startup(dp):
    print("Started!")


if __name__ == '__main__':
    from aiogram import executor
    from bot.handlers import dp
    executor.start_polling(dp, on_startup=on_startup, on_shutdown=on_shutdown)
