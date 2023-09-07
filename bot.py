import time
from aiogram import Bot, Dispatcher, F
from  aiogram.types import Message
from aiogram.utils.markdown import hbold, hlink
import asyncio
import logging
from  tokens import TOKEN


def post_to_telegram(products):
    logging.basicConfig(level=logging.INFO)

    bot = Bot(token=TOKEN, parse_mode='HTML')
    dp = Dispatcher()

    @dp.message(F.text == '/start')
    async def cmd_start(message:Message):
        await message.answer(f'Hello, {message.from_user.first_name} !')
        for product in products:
            card = f' {hlink(product["title"], product["link"])}\n' \
                f'{hbold("Price:")} {product["price"]}\n' \
                f'{hbold("Status:")} {product["status"]}'
            await message.answer(card)
            time.sleep(1)

    async def starting():
        await dp.start_polling(bot)

    asyncio.run(starting())