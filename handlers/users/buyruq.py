from aiogram import types
from keyboards.default.buyruq import buyruq
from loader import dp
@dp.message_handler(text='📢Buyruqlar')
async def bot_start(message: types.Message):
    await message.answer("<b>Buyruqlar 👇</b>", reply_markup=buyruq)
