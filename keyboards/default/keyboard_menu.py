from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

kb_menu = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='10'),
            KeyboardButton(text='11')
        ],
        [
            KeyboardButton(text='100')
        ],
        [
            KeyboardButton(text='Инлайн меню'),
            KeyboardButton(text='Хай'),
            KeyboardButton(text='Чо каво')
        ]
    ],
    resize_keyboard=True
)