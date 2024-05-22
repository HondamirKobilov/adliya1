from aiogram import types
from keyboards.default.shartnomaTahrirlash import shartnomaTahrir
from loader import dp
@dp.message_handler(text='1.Shartnomalar')
async def orqaga(message: types.Message):
    await message.answer("Kerakli bo'limni tanlang 👇", reply_markup=shartnomaTahrir)
