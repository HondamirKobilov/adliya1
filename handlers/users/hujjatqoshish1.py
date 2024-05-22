from aiogram import types
from loader import dp, bot
from keyboards.default.hujjatlarQoshish import hujjatlar
@dp.message_handler(text='Shartnoma qo\'shish')
async def add_data(message: types.Message):
    await message.answer("Qaysi turdagi fayl qo'shmoqchisiz", reply_markup=hujjatlar)
