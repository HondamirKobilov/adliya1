from aiogram import types
from keyboards.default.buyruqTahrirlash import buyruqTahrir
from loader import dp
@dp.message_handler(text='2.Buyruqlar')
async def orqaga(message: types.Message):
    await message.answer("Kerakli bo'limni tanlang 👇", reply_markup=buyruqTahrir)
