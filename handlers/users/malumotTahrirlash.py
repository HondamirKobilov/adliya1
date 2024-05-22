from aiogram import types
from keyboards.default.shartnoma import shartnoma
from loader import dp
@dp.message_handler(text='Ma\'lumot tahrirlash')
async def bot_start(message: types.Message):
    await message.answer("⚙️...")
