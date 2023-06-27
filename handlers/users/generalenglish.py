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


@dp.message_handler(commands='generalvideo')
async def ieltsturbovideo(message: types.Message):
    video1 = 'BAACAgIAAxkBAAJEXmSYfg-goFTVdFGXGwJ2XJ1ajmsTAAKEMQAC4IHJSGybJSUfqUoLLwQ'

    await bot.send_video(chat_id=message.chat.id, video=video1)

# @dp.message_handler(commands='generalenglish', state=None)
# async def generalenglish(message: types.Message):
#     text = ("<b>Founders Language Schoolga</b> xush kelibsiz!\n\n"
#             "📹 Agarda <b>video</b> formatda ko'rishni istasangiz xohlagan so'z, yuboring.\n\n"
#             "Bizning General English kurs afzalliklarimizni sanab o'tamiz:\n"
#             "✅ Guruhda 10 ± ta o'quvchi bo'ladi\n"
#             "✅ Oxford Press nashriyotlari\n"
#             "✅ Shaxsiy kabinetingizga ega bo'lasiz\n"
#             "✅ Audio lug'at\n"
#             "✅ Qo'shimcha ikkinchi ustoz\n"
#             "✅ Darslar davomiyligi 2 soatdan\n\n"
#             "😊 Bizning kurslarimiz sizning yorqin kelajagingiz uchun <b>imkoniyatlar eshigini</b> ochishga yordam beradi.\n\n")
    
#     await message.answer(text)
#     await Medias.generalvideo.set()

# @dp.message_handler(state=Medias.generalvideo)
# async def send_video(message: types.Message, state: FSMContext):

#     video1 = 'BAACAgIAAxkBAAJDyWSW0i3IwHhsXV2_y_ermKVG2zPHAAKpLwAC4IG5SI_DTJQ4v0QHLwQ' #videoid

#     await bot.send_video(chat_id=message.chat.id, video=video1)
#     await state.finish()
    