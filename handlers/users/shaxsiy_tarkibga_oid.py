from aiogram import types
from aiogram.types import InputFile
from loader import dp, db
import tempfile
import os

@dp.message_handler(text='Shaxsiy tarkibga oid')
async def bot_start(message: types.Message):
    await message.answer("⚙️ Fayl yuklanmoqda...")

    # Bazadan fayllarni olish
    shaxsiy_tarkib = await db.get_all_shaxsiyTarkib()

    if not shaxsiy_tarkib:
        await message.answer("Hech qanday shaxsiy tarkibga oid fayl topilmadi.")
    else:
        files_to_send = []
        for bitim in shaxsiy_tarkib:
            # Extract file data and filename
            file_content = bitim['data3']
            filename = bitim['fayl3']

            # Create a temporary file
            with tempfile.NamedTemporaryFile(delete=False) as temp_file:
                temp_file.write(file_content)
                temp_file_path = temp_file.name

            files_to_send.append((temp_file_path, filename))

        # Send the files
        for file_path, filename in files_to_send:
            await message.answer_document(InputFile(file_path, filename=filename))
            os.remove(file_path)  # Clean up the temporary file
