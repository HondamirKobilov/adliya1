from aiogram import types
from keyboards.default.boshMenu import boshMenu
from loader import dp
@dp.message_handler(text='🔙Ortga')
async def orqaga(message: types.Message):
    await message.answer("Kerakli bo'limni tanlang 👇", reply_markup=boshMenu)
