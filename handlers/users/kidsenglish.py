from aiogram import types
from states.register import Medias
from aiogram.dispatcher import FSMContext
from loader import dp, bot

@dp.message_handler(commands='kidsenglish')
async def kidsenglish(message: types.Message):
    text = ("<b>Founders Language Schoolga</b> xush kelibsiz!\n\n"
            "KIDS English kurslari ning afzalliklarini sanab o'tamiz:\n\n"
            "✅ Guruhda 10 ± ta o'quvchi bo'ladi\n"
            "✅ KIDS guruhlari har bir darajada 4 oy va darslar davomiyligi 2 soatdan\n"
            "✅ Angliya metodikasi orqali ta'lim\n"
            "✅ Macmillan nashriyot kitoblari\n"
            "✅ Ota-ona nazorati uchun shaxsiy kabinet\n"
            "✅ Hero Card (ushbu Hero Card larni yig'gan holda siz <b>Founders</b> o'quv markazining qimmatbaho sov'g'alariga ega bo'lasiz)\n"
            "✅ Ikkinchi ustoz biriktriladi\n\n"
            "Ha aytgancha har oyning 2 ta yakshanba kunlari <b>jajji bolajonlarimiz</b> vaqtini behuda o'tkazmasin degan holda biz <b>bepul</b> 'event' lar o'tkazamiz\n\n"
            "😌 <b>Founders</b> da farzandigiz kelajagini birgalikda quramiz\n\n")
    
    await message.answer(text)

@dp.message_handler(commands='kidsvideo')
async def ieltsturbovideo(message: types.Message):
    video1 = 'BAACAgIAAxkBAAJEs2ScQyxu_DfCeP7lQ3uNnax3BtWEAAIZLgACW3PhSIpLKslWuHi3LwQ'

    await bot.send_video(chat_id=message.chat.id, video=video1)

# @dp.message_handler(commands='kidsenglish', state=None)
# async def kidsenglish(message: types.Message):
#     text = ("<b>Founders Language Schoolga</b> xush kelibsiz!\n\n"
#             "📹 Agarda <b>video formatda</b> ko'rishni istasangiz xohlagan <b>so'z,</b> yuboring\n\n"
#             "KIDS English kurslari ning afzalliklarini sanab o'tamiz:\n\n"
#             "✅ Guruhda 10 ± ta o'quvchi bo'ladi\n"
#             "✅ KIDS guruhlari har bir darajada 4 oy va darslar davomiyligi 2 soatdan\n"
#             "✅ Angliya metodikasi orqali ta'lim\n"
#             "✅ Macmillan nashriyot kitoblari\n"
#             "✅ Ota-ona nazorati uchun shaxsiy kabinet\n"
#             "✅ Hero Card (ushbu Hero Card larni yig'gan holda siz <b>Founders</b> o'quv markazining qimmatbaho sov'g'alariga ega bo'lasiz)\n"
#             "✅ Ikkinchi ustoz biriktriladi\n\n"
#             "Ha aytgancha har oyning 2 ta yakshanba kunlari <b>jajji bolajonlarimiz</b> vaqtini behuda o'tkazmasin degan holda biz <b>bepul</b> 'event' lar o'tkazamiz\n\n"
#             "😌 <b>Founders</b> da farzandigiz kelajagini birgalikda quramiz\n\n")
    
#     await message.answer(text)
#     await Medias.kidsvideo.set()

# @dp.message_handler(state=Medias.kidsvideo)
# async def send_video(message: types.Message, state: FSMContext):

#     video1 = 'BAACAgIAAxkBAAJDymSW0kFGBXO8XQoH2fzDfFJUKCB0AAKrLwAC4IG5SPFTkwABHzE-Yi8E'  # video ID

#     await bot.send_video(chat_id=message.chat.id, video=video1)
#     await state.finish()
