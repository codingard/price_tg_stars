from aiogram import Bot, Dispatcher
import asyncio
import handlers.price
from config import BOT_TOKEN

async def main():
    bot = Bot(token = BOT_TOKEN)
    dp = Dispatcher()
    dp.include_routers(
        handlers.price.router
    )

    await dp.start_polling(bot)

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except Exception as e:
        print(e)