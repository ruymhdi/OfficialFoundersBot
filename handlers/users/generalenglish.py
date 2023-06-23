from aiogram.types import ContentTypes
from states.register import Medias
from aiogram.dispatcher import FSMContext
from aiogram.types import ReplyKeyboardRemove
from aiogram import types
from loader import dp, bot
from handlers.users.help import bot_help


@dp.message_handler(commands='generalenglish', state=None)
async def generalenglish(message: types.Message):
    text = ("<b>Founders Language Schoolga</b> xush kelibsiz!\n\n"
            "📹 Agarda <b>video</b> formatda ko'rishni istasangiz xohlagan so'z, yuboring.\n\n"
            "Bizning General English kurs afzalliklarimizni sanab o'tamiz:\n"
            "✅ Guruhda 10 ± ta o'quvchi bo'ladi\n"
            "✅ Oxford Press nashriyotlari\n"
            "✅ Shaxsiy kabinetingizga ega bo'lasiz\n"
            "✅ Audio lug'at\n"
            "✅ Qo'shimcha ikkinchi ustoz\n"
            "✅ Darslar davomiyligi 2 soatdan\n"
            "😊 Bizning kurslarimiz sizning yorqin kelajagingiz uchun <b>imkoniyatlar eshigini</b> ochishga yordam beradi.")
    
    await message.answer(text)
    await Medias.generalvideo.set()

@dp.message_handler(state=Medias.generalvideo)
async def send_video(message: types.Message, state: FSMContext):

    video1 = 'BAACAgIAAxkBAAJCe2SVYoJsQfGSwgQ455lT0qEgjs8mAALHMgACj4uxSAxlwxNwElkzLwQ' #videoid

    await bot.send_video(chat_id=message.chat.id, video=video1)
    await state.finish()
