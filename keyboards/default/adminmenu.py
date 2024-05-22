from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
adminmenu = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='Ma\'lumot qo\'shish'),
            KeyboardButton(text='Ma\'lumot tahrirlash')
        ],
    ],
    resize_keyboard=True
)
