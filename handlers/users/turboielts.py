from aiogram import types
from states.register import Medias
from aiogram.dispatcher import FSMContext
from loader import dp, bot


@dp.message_handler(commands='ieltsturbo', state=None)
async def ieltsturbo(message: types.Message):
    text = ("<b>Founders Language Schoolga</b> xush kelibsiz!\n\n"
            "📹 Agarda <b>video formatda</b> ko'rishni istasangiz xohlagan <b>so'z,</b> yuboring\n\n"
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
    await Medias.iltesturbo.set()

@dp.message_handler(state=Medias.iltesturbo)
async def send_video(message: types.Message, state: FSMContext):
    
    video1 = 'BAACAgIAAxkBAAJCsGSVgEhSGW_qRDnH12cm-8kizwHvAAL1NAACj4uxSKv4sVZMe2pYLwQ' #videoid

    await bot.send_video(chat_id=message.chat.id, video=video1)
    await state.finish()
