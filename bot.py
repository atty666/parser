from aiogram import Bot, Dispatcher, F
from  aiogram.types import Message
import asyncio
import logging
from  tokens import TOKEN

def post_to_telegram(products):
    logging.basicConfig(level=logging.INFO)

    bot = Bot(token=TOKEN)
    dp = Dispatcher()

    @dp.message(F.text == '/start')
    async def cmd_start(message:Message):
        await message.answer(f'Hello, {message.from_user.first_name} !')
        for product in products:
            await message.answer(product['title'])#, \
                                 #product['price'], \
                                 #product['status'], \
                                 #product['link'])


    async def starting():
        await dp.start_polling(bot)

    asyncio.run(starting())