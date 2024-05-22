from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
adminmenu1 = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='Shartnoma qo\'shish'),
            KeyboardButton(text='Buyruq qo\'shish')
        ],
        [
            KeyboardButton(text='⬅️Asosiy menyuga')
        ],
    ],
    resize_keyboard=True
)
