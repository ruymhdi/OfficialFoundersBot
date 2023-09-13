from aiogram import types
from loader import dp, bot

@dp.message_handler(commands='register')
async def start(message: types.Message):
    await message.answer("<b>Founders Language Schoolga</b> ro'yxatdan o'tmoqchimisiz?\n\n"
                         "Unday bo'lsa quyidagi formani to'ldiring:\n"
                         "👉 Havola: form.foundersschool.uz\n\n"
                         "Biz sizni markazimizda ko'rishni intizorlik bilan kutamiz!")
