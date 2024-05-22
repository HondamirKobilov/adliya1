from aiogram import types
from keyboards.default.tahrirlash import tahrirlash
from loader import dp
@dp.message_handler(text='Ma\'lumot tahrirlash')
async def orqaga(message: types.Message):
    await message.answer("Kerakli bo'limni tanlang 👇", reply_markup=tahrirlash)
