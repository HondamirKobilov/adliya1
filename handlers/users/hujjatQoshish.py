from aiogram import types
from loader import dp, bot
from keyboards.default.adminmenu1 import adminmenu1
@dp.message_handler(text='Ma\'lumot qo\'shish')
async def add_data(message: types.Message):
    await message.answer("Shartnoma qo'shasizmi yoki Buyruq", reply_markup=adminmenu1)

