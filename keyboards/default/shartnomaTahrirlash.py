from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
shartnomaTahrir = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='📝Mehnat munosabatlari'),
            KeyboardButton(text='📝Fuqarolik shartnomasi')
        ],
        [
            KeyboardButton(text='📝Kelishuv bitimlari'),
        ],
        [
            KeyboardButton(text='⬅️Ortga'),
        ],
    ],
    resize_keyboard=True
)
