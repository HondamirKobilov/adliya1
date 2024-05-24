from aiogram import types
from keyboards.default.adminmenu import adminmenu
from loader import dp
@dp.message_handler(text='🔙ortga')
async def orqaga(message: types.Message):
    await message.answer("Kerakli bo'limni tanlang 👇", reply_markup=adminmenu)
