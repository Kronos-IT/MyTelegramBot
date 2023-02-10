from aiogram import Bot, types, Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage

from data import config

# Создаём переменную бота где Bot(token='Токен вашего бота'
bot = Bot(token=config.BOT_TOKEN, parse_mode=types.ParseMode.HTML)

storage = MemoryStorage()

# Создаём диспетчер
dp = Dispatcher(bot, storage=storage)