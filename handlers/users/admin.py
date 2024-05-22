from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart
from loader import dp
from keyboards.default.adminmenu import adminmenu
admin_user_ids = [1405814595]
@dp.message_handler(CommandStart(), user_id=admin_user_ids)
async def admin_start(message: types.Message):
    await message.answer("Admin panelga xush kelibsiz", reply_markup=adminmenu)
