from aiogram.types import Message
from services.price_stars import PriceStars
from config import CURRENCY_ALIASES

async def output_result(message: Message, currency_input, amount):
    try:
        price = PriceStars()
    except Exception as e:
        await message.answer(f"Ошибка при получении цен: {e}")
        return
    
    currency_code = CURRENCY_ALIASES[currency_input]

    try:
        if currency_code == "TON":
            result = price.ton_to_stars(amount)
            await message.answer(f'{amount} TON в Stars: {result:.2f}')
        elif currency_code == "USDT":
            result = price.usdt_to_stars(amount)
            await message.answer(f'{amount} USDT в Stars: {result:.2f}')
        elif currency_code == "STARS":
            result_usdt = price.stars_to_usdt(amount)
            result_ton = price.stars_to_ton(amount)
            await message.answer(f'{amount} Stars в USDT: {result_usdt:.2f}\n{amount} Stars в TON: {result_ton:.2f}')
    except Exception as e:
        await message.answer(f"Ошибка при расчётах: {e}")