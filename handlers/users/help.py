from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandHelp

from loader import dp


@dp.message_handler(CommandHelp())
async def bot_help(message: types.Message):
    text = ("@founders_school_uz let's grow with us!\n",
            "<b>Asosiy:</b>",
            "/start - Botni ishga tushirish",
            "/help - Shu habarni ko'rsatadi\n\n<b>Biz haqimizda:</b>",
            "/aboutus - Biz haqimizda:\n"
            "/aboutadresses - Bizning manzillar\n\n"
            "<b>Bizning kurslar:</b>\n"
            "/ieltsturbo - IELTS Turbo\n"
            "/ieltsvideo - IELTS Turbo <b>video</b>\n\n"
            "/generalenglish - General English\n"
            "/generalvideo - General English <b>video</b>\n\n"
            "/kidsenglish - KIDS English\n"
            "/kidsvideo - KIDS English <b>video</b>\n\n"
            "<b>Regestratiya:</b>\n"
            "/register - Registratsiydan o'tish")
    
    await message.answer("\n".join(text))
