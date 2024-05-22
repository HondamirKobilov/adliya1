from aiogram import types
from loader import dp, bot, db
from keyboards.default.adminmenu1 import adminmenu1

# Fayllarni o'chirish uchun handlerlar
@dp.message_handler(text='📝Kelishuv bitimlari')
async def delete_kelishuv_bitimlari(message: types.Message):
    await db.delete_all_kelishuvBitimlari("kelishuvBitimlari")
    await message.answer("Kelishuv bitimlari bazasidagi barcha ma'lumotlar o'chirildi.")
    await message.answer("Kerakli bo'limni tanlang 👇.", reply_markup=adminmenu1)

@dp.message_handler(text='📝Mehnat munosabatlari')
async def delete_mehnat_munosabatlari(message: types.Message):
    await db.delete_all_mehnatMunosabatlari('mehnatMunosabatlari')
    await message.answer("Mehnat munosabatlari bazasidagi barcha ma'lumotlar o'chirildi.")
    await message.answer("Kerakli bo'limni tanlang 👇.", reply_markup=adminmenu1)

@dp.message_handler(text='📝Fuqarolik shartnomasi')
async def delete_fuqorolik_shartnomasi(message: types.Message):
    await db.delete_all_fuqorolikShartnomasi("fuqorolikShartnomasi")
    await message.answer("Fuqarolik shartnomasi bazasidagi barcha ma'lumotlar o'chirildi.")
    await message.answer("Kerakli bo'limni tanlang 👇.", reply_markup=adminmenu1)

@dp.message_handler(text='📝Shaxsiy tarkibga oid')
async def delete_shaxsiy_tarkib(message: types.Message):
    await db.delete_all_shaxsiyTarkib("shaxsiyTarkib")
    await message.answer("Shaxsiy tarkib bazasidagi barcha ma'lumotlar o'chirildi.")
    await message.answer("Kerakli bo'limni tanlang 👇.", reply_markup=adminmenu1)

@dp.message_handler(text='📝Ta\'tillarga oid')
async def delete_tatil(message: types.Message):
    await db.delete_all_tatil("tatil")
    await message.answer("Ta'til bazasidagi barcha ma'lumotlar o'chirildi.")
    await message.answer("Kerakli bo'limni tanlang 👇.", reply_markup=adminmenu1)

@dp.message_handler(text='📝Umumiy masalalarga oid')
async def delete_umumiy_masala(message: types.Message):
    await db.delete_all_umumiyMasala("umumiyMasala")
    await message.answer("Umumiy masalalar bazasidagi barcha ma'lumotlar o'chirildi.")
    await message.answer("Kerakli bo'limni tanlang 👇.", reply_markup=adminmenu1)
