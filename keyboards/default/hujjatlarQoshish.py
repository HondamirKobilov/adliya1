from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
hujjatlar = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='1.Mehnat munosabatlari'),
            KeyboardButton(text='2.Fuqarolik shartnomasi')
        ],
        [
            KeyboardButton(text='3.Kelishuv bitimlari'),
        ],
        [
            KeyboardButton(text='🔙ortga'),
        ],
    ],
    resize_keyboard=True
)
