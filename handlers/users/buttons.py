from aiogram import types

from loader import dp

@dp.message_handler(text='10')
async def buttons_test(message: types.Message):
    await message.answer(f'Тест кнопки')