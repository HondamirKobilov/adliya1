# from aiogram import types
# from loader import dp, bot, db
#
# # Fayl turini aniqlash uchun global o'zgaruvchi
# current_file_type = None
# @dp.message_handler(text='1.Shaxsiy tarkibga oid')
# async def sharQosh1(message: types.Message):
#     global current_file_type
#     current_file_type = 'shaxsiyTarkib'
#     await db.create_table_shaxsiyTarkib()
#     await message.answer("PDF yoki DOCX formatdagi fayl yuboring aka")
#
# @dp.message_handler(text='2.Ta\'tillarga oid')
# async def sharQosh2(message: types.Message):
#     global current_file_type
#     current_file_type = 'tatil'
#     await db.create_table_tatil()
#     await message.answer("PDF yoki DOCX formatdagi fayl yuboring")
#
# @dp.message_handler(text='3.Umumiy masalalarga oid')
# async def sharQosh3(message: types.Message):
#     global current_file_type
#     current_file_type = 'umumiyMasala'
#     await db.create_table_umumiyMasala()
#     await message.answer("PDF yoki DOCX formatdagi fayl yuboring")
# @dp.message_handler(content_types=['document'])
# async def handle_document(message: types.Message):
#     global current_file_type
#
#     document = message.document
#     file_id = document.file_id
#     file_name = document.file_name
#     caption = message.caption if message.caption else file_name  # caption mavjud bo'lmasa file_name oling
#
#     if document.mime_type in ['application/pdf',
#                               'application/vnd.openxmlformats-officedocument.wordprocessingml.document']:
#         file = await bot.get_file(file_id)
#         file_path = file.file_path
#
#         # Faylni yuklab olish va saqlash
#         file_data = await bot.download_file(file_path)
#         binary_data = file_data.read()  # Faylni binary shaklida o'qish
#
#         if current_file_type == 'shaxsiyTarkib':
#             await db.add_shaxsiyTarkib(fayl3=caption, data3=binary_data)
#             await message.answer("Fayl shaxs tarkibiga oid bazasiga saqlandi.")
#         elif current_file_type == 'tatil':
#             await db.add_tatil(fayl4=caption, data4=binary_data)
#             await message.answer("Fayl tatilga oid bazasiga saqlandi.")
#         elif current_file_type == 'umumiyMasala':
#             await db.add_umumiyMasala(fayl5=caption, data5=binary_data)
#             await message.answer("Fayl umumiy masalalarga oid bazasiga saqlandi.")
#         else:
#             await message.answer("Xatolik: fayl turi aniqlanmadi seni koding xato")
#     else:
#         await message.answer("Kechirasiz, faqat PDF yoki DOCX formatdagi fayllarni yuboring.")
#
