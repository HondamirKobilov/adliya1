from aiogram import types
from loader import dp, bot, db

# Fayl turini aniqlash uchun global o'zgaruvchi
current_file_type = None

# 3.Kelishuv bitimlari, 1.Mehnat munosabatlari, 2.Fuqarolik shartnomasi uchun handlerlar
@dp.message_handler(text='3.Kelishuv bitimlari')
async def kelishuv_bitimlari(message: types.Message):
    global current_file_type
    current_file_type = 'kelishuvbitimlari'
    await message.answer("PDF yoki DOCX formatdagi fayl yuboring")

@dp.message_handler(text='1.Mehnat munosabatlari')
async def mehnat_munosabatlari(message: types.Message):
    global current_file_type
    current_file_type = 'mehnatmunosabatlari'
    await message.answer("PDF yoki DOCX formatdagi fayl yuboring")

@dp.message_handler(text='2.Fuqarolik shartnomasi')
async def fuqorolik_shartnomasi(message: types.Message):
    global current_file_type
    current_file_type = 'fuqorolikshartnomasi'
    await message.answer("PDF yoki DOCX formatdagi fayl yuboring")

# 1.Shaxsiy tarkibga oid, 2.Ta'tillarga oid, 3.Umumiy masalalarga oid uchun handlerlar
@dp.message_handler(text='1.Shaxsiy tarkibga oid')
async def shaxsiy_tarkib(message: types.Message):
    global current_file_type
    current_file_type = 'shaxsiytarkib'
    await db.create_table_shaxsiyTarkib()
    await message.answer("PDF yoki DOCX formatdagi fayl yuboring aka")

@dp.message_handler(text='2.Ta\'tillarga oid')
async def tatil(message: types.Message):
    global current_file_type
    current_file_type = 'tatil'
    await db.create_table_tatil()
    await message.answer("PDF yoki DOCX formatdagi fayl yuboring")

@dp.message_handler(text='3.Umumiy masalalarga oid')
async def umumiy_masala(message: types.Message):
    global current_file_type
    current_file_type = 'umumiymasala'
    await db.create_table_umumiyMasala()
    await message.answer("PDF yoki DOCX formatdagi fayl yuboring")

@dp.message_handler(content_types=['document'])
async def handle_document(message: types.Message):
    global current_file_type

    document = message.document
    file_id = document.file_id
    file_name = document.file_name
    caption = message.caption if message.caption else file_name

    if document.mime_type in ['application/pdf', 'application/vnd.openxmlformats-officedocument.wordprocessingml.document']:
        file = await bot.get_file(file_id)
        file_path = file.file_path

        # Faylni yuklab olish va saqlash
        file_data = await bot.download_file(file_path)
        binary_data = file_data.read()

        if current_file_type == 'kelishuvbitimlari':
            await db.create_table_kelishuvBitim() if not await db.table_exists('kelishuvbitimlari') else None
            await db.add_kelishuvBitimlari(fayl=caption, data=binary_data)
            await message.answer("Fayl kelishuv bitimlari bazasiga saqlandi.")
        elif current_file_type == 'mehnatmunosabatlari':
            await db.create_table_mehnatMunosabatlari() if not await db.table_exists('mehnatmunosabatlari') else None
            await db.add_mehnatMunosabatlari(fayl1=caption, data1=binary_data)
            await message.answer("Fayl mehnat munosabatlari bazasiga saqlandi.")
        elif current_file_type == 'fuqorolikshartnomasi':
            await db.create_table_fuqorolikShartnomasi() if not await db.table_exists('fuqorolikshartnomasi') else None
            await db.add_fuqorolikShartnomasi(fayl2=caption, data2=binary_data)
            await message.answer("Fayl fuqorolik shartnomasi bazasiga saqlandi.")
        elif current_file_type == 'shaxsiytarkib':
            await db.add_shaxsiyTarkib(fayl3=caption, data3=binary_data)
            await message.answer("Fayl shaxs tarkibiga oid bazasiga saqlandi.")
        elif current_file_type == 'tatil':
            await db.add_tatil(fayl4=caption, data4=binary_data)
            await message.answer("Fayl tatilga oid bazasiga saqlandi.")
        elif current_file_type == 'umumiymasala':
            await db.add_umumiyMasala(fayl5=caption, data5=binary_data)
            await message.answer("Fayl umumiy masalalarga oid bazasiga saqlandi.")
        else:
            await message.answer("Xatolik: fayl turi aniqlanmadi")
    else:
        await message.answer("Kechirasiz, faqat PDF yoki DOCX formatdagi fayllarni yuboring.")
