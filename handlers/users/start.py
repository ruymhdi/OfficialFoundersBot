from aiogram import types
from loader import dp, bot
from aiogram.dispatcher.filters.builtin import CommandStart



@dp.message_handler(CommandStart())
async def start_command(message: types.Message):
    await message.answer(f"Assalomu alaykum! <b>{message.from_user.full_name}</b>\n\n"
                         f"<b>Botimiz siz nimalar bera oladi?</b>\n\n"
                         f"1. Avvalo o'quv markazimizda qanday kurslar mavjudligi ham <b>matn</b> ham video <b>sifatida</b>\n"
                         f"2. O'quv markazimizning <b>lokatsion joylashuvi</b>\n"
                         f"3. O'quv kurslarimizga <b>ro'yxatdan o'tishingiz mumkin</b>\n"
                         f"4. <b>Taklif yoki shikoyatingizni</b> ham qoldirishingiz mumkin bo'ladi!\n\n"
                         f"<b>Botdan foydalanish</b> uchun shunchaki /help buyrug'ini bering va ko'rsatilgan <b>buyruqlardan</b> sizga kerakli bo'lgan biror birini tanlashingiz mumkin bo'ladi.")
