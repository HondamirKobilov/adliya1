from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
boshMenu = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='📑Shartnomalar'),
            KeyboardButton(text='📢Buyruqlar')
        ],
    ],
    resize_keyboard=True
)
