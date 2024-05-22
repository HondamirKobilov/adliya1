from aiogram.types import Message
from aiogram.dispatcher.filters import Command
from loader import dp
from keyboards.default.boshMenu import boshMenu

@dp.message_handler(Command("start"))
async def bosh_menu(message: Message):
    await message.answer("<b>Assalomu alaykum</b>", reply_markup=boshMenu)
