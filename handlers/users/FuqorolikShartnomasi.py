from aiogram import types
from aiogram.types import InputFile
from loader import dp, db
import tempfile
import os

@dp.message_handler(text='Fuqarolik shartnomasi')
async def bot_start(message: types.Message):
    await message.answer("⚙️ Fayl yuklanmoqda...")

    # Bazadan fayllarni olish
    fuqorolik_shartnomasi = await db.get_all_fuqorolikShartnomasi()

    if not fuqorolik_shartnomasi:
        await message.answer("Hech qanday fuqorolik shartnomasiga oid fayl topilmadi.")
    else:
        files_to_send = []
        for bitim in fuqorolik_shartnomasi:
            # Extract file data and filename
            file_content = bitim['data2']
            filename = bitim['fayl2']

            # Create a temporary file
            with tempfile.NamedTemporaryFile(delete=False) as temp_file:
                temp_file.write(file_content)
                temp_file_path = temp_file.name

            files_to_send.append((temp_file_path, filename))

        # Send the files
        for file_path, filename in files_to_send:
            await message.answer_document(InputFile(file_path, filename=filename))
            os.remove(file_path)  # Clean up the temporary file
