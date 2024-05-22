from aiogram import types
from keyboards.default.adminmenu1 import adminmenu1
from loader import dp
@dp.message_handler(text='🔙ortga')
async def orqaga(message: types.Message):
    await message.answer("Kerakli bo'limni tanlang 👇", reply_markup=adminmenu1)
