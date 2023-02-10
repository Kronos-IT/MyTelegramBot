from aiogram import types

from loader import dp

@dp.message_handler(text='Привет')
async def command_hello(message: types.Message):
    await message.answer(f'Привет, как дела?')