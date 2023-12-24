from aiogram.types import ContentTypes
from states.register import Medias
from aiogram.dispatcher import FSMContext
from aiogram.types import ReplyKeyboardRemove
from aiogram import types
from loader import dp, bot
from handlers.users.help import bot_help

@dp.message_handler(commands='generalenglish')
async def generalenglish(message: types.Message):
    text = ("<b>Founders Language Schoolga</b> xush kelibsiz!\n\n"
            "Bizning General English kurs afzalliklarimizni sanab o'tamiz:\n"
            "✅ Guruhda 10 ± ta o'quvchi bo'ladi\n"
            "✅ Oxford Press nashriyotlari\n"
            "✅ Shaxsiy kabinetingizga ega bo'lasiz\n"
            "✅ Audio lug'at\n"
            "✅ Qo'shimcha ikkinchi ustoz\n"
            "✅ Darslar davomiyligi 2 soatdan\n\n"
            "😊 Bizning kurslarimiz sizning yorqin kelajagingiz uchun <b>imkoniyatlar eshigini</b> ochishga yordam beradi.\n\n")
    
    await message.answer(text)

    text2 = ("@founders_school_uz let's grow with us!\n",
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
            "/register - Registratsiydan o'tish\n",
            "<b>Sifat nazorati:</b>\n"
            "/suggest - Taklif va shikoyat uchun")

    await message.answer("\n".join(text2))



@dp.message_handler(commands='generalvideo')
async def ieltsturbovideo(message: types.Message):
    video1 = 'BAACAgIAAxkBAAJEXmSYfg-goFTVdFGXGwJ2XJ1ajmsTAAKEMQAC4IHJSGybJSUfqUoLLwQ'

    await bot.send_video(chat_id=message.chat.id, video=video1)
