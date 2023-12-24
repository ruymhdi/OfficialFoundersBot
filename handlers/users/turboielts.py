from aiogram import types
from states.register import Medias
from aiogram.dispatcher import FSMContext
from loader import dp, bot


@dp.message_handler(commands='ieltsturbo')
async def ieltsturbo(message: types.Message):
    text = ("<b>Founders Language Schoolga</b> xush kelibsiz!\n\n"
            "🔥 Bizning IELTS Turbo kursimiz 2 oydan 3 oygacha davom etadi\n\n"
            "IELTS Turbo kurslarimiz afzalliklari quyidagilar:\n\n"
            "✅ Guruhda 10 ± ta o'quvchi bo'ladi\n"
            "✅ Founders o'quv markazi tuzib chiqqan 6 ta maxsus IELTS kitoblari\n"
            "✅ Shaxsiy kabinet\n"
            "✅ Yordamchi ustoz\n"
            "✅ Mock imtihonlar\n\n"
            "Bizning <b>samarali darslarimiz</b>, intensiv mashg'ulotlarimiz va <b>foydali</b> o'quv materiallarimiz sizning o'rganish jarayoningizni <b>sifatli va tezkor</b> tarzda boshqarishga yordam beradi. O'zlashtirilgan o'qitish usullarimiz va shaxsiy qo'llab-quvvatlashimiz orqali siz tez va samarali o'rganishni boshlaysiz.\n\n"
            "😉 Bizning <b>qisqa va intensiv</b> dars jadvalimiz sizning ish yoki o'qish rejangizga moslab tuziladi. Siz ishlayotgan yoki o'qiyotgan bo'lsangiz ham, biz sizning dars vaqtingizni moslashtirish uchun qulay vaqtlar taklif etamiz.")

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



@dp.message_handler(commands='ieltsvideo')
async def ieltsturbovideo(message: types.Message):
    video1 = 'BAACAgIAAxkBAAJEWGSYeZhEhGkjULwlAAGpq3lhB4gZXwACHzEAAuCByUjTDzOikKkSQy8E'

    await bot.send_video(chat_id=message.chat.id, video=video1)
