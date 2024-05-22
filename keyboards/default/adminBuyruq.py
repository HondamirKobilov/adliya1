from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
adminBuyruqlar = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='1.Shaxsiy tarkibga oid'),
            KeyboardButton(text='2.Ta\'tillarga oid')
        ],
        [
            KeyboardButton(text='3.Umumiy masalalarga oid')
        ],
        [
            KeyboardButton(text='🔙ortga'),
        ],
    ],
    resize_keyboard=True
)
