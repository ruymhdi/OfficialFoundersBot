from aiogram.types import ContentTypes
from states.register import Medias
from aiogram.dispatcher import FSMContext
from aiogram.types import ReplyKeyboardRemove
from aiogram import types
from loader import dp, bot
from handlers.users.help import bot_help


@dp.message_handler(commands='generalenglish', state=None)
async def generalenglish(message: types.Message):
<<<<<<< HEAD
    text = ("Founders Language Schoolga xush kelibsiz!\n\n"
            "📹 Agarda video formatda ko'rishni istasangiz xohlagan so'z, yuboring.\n\n"
            "Bizning General English kurs afzalliklarimizni sanab o'tamiz:\n"
            "✅ Guruhda 10 ± ta o'quvchi bo'ladi\n"
            "✅ Oxford Press nashriyotlari\n"
            "✅ Shaxsiy kabinetingizga ega bo'lasiz\n"
            "✅ Audio lug'at\n"
            "✅ Qo'shimcha ikkinchi ustoz\n"
            "✅ Darslar davomiyligi 2 soatdan\n"
            "😊 Bizning kurslarimiz sizning yorqin kelajagingiz uchun imkoniyatlar eshigini ochishga yordam beradi."
=======
    text = ("<b>Founders Language Schoolga</b>"
            "✅ Yordamchi ustoz biriktiriladi\n"
            "✅ Darslar 2 soatdan\n\n"
            "✅ Har bir kurs 2 oy davom etadi\n"
            "📹 Agarda <b>video formatda</b> ko'rishni istasangiz 1 <b>raqamini yuboring</b>\n\n"
            "😊 Bizning kurslar barchaga, tezroq <b>IELTS</b> dan yaxshi natija va universitetga talab qilinayotgan ball ni qo'lga kiritishga yordam beradi\n\n"
>>>>>>> 2c3047ec6ccbed1a3d5312d5ad3a43866b02365f
            )
    
    await message.answer(text)
    await Medias.generalvideo.set()

@dp.message_handler(state=Medias.generalvideo)
async def send_video(message: types.Message, state: FSMContext):

    video1 = 'BAACAgIAAxkBAAJCe2SVYoJsQfGSwgQ455lT0qEgjs8mAALHMgACj4uxSAxlwxNwElkzLwQ' #videoid

    await bot.send_video(chat_id=message.chat.id, video=video1)
    await state.finish()
