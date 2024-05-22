from aiogram import types
from loader import dp, bot
from keyboards.default.adminBuyruq import adminBuyruqlar
@dp.message_handler(text='Buyruq qo\'shish')
async def add_data(message: types.Message):
    await message.answer("Qaysi turdagi buyruq qo'shmoqchisiz", reply_markup=adminBuyruqlar)
