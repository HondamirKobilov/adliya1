from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
tahrirlash = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='1.Shartnomalar'),
            KeyboardButton(text='2.Buyruqlar')
        ],
        [
            KeyboardButton(text='🔙ortga'),
        ],
    ],
    resize_keyboard=True
)
