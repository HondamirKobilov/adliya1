from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
buyruq = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='Shaxsiy tarkibga oid'),
            KeyboardButton(text='Ta\'tillarga oid')
        ],
        [
            KeyboardButton(text='Umumiy masalalarga oid'),
        ],
        [
            KeyboardButton(text='🔙Ortga'),
        ],
    ],
    resize_keyboard=True
)
