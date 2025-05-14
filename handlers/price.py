from aiogram import Router
from aiogram.types import Message

from services.output import output_result
from services.processing import processing

router = Router()

@router.message()
async def calculate(message: Message):
    text = message.text.strip()
    result = processing(text)
    if result:
        amount_raw, currency_input = result
        await output_result(message=message, amount=amount_raw, currency_input=currency_input)
