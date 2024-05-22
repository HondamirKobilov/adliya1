from aiogram import types
from keyboards.default.shartnoma import shartnoma
from loader import dp
@dp.message_handler(text='📑Shartnomalar')
async def bot_start(message: types.Message):
    await message.answer("<b>Shartnomalar 👇</b>", reply_markup=shartnoma)
