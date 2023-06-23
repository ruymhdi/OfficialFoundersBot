# from states.register import Lists
# from aiogram import types
# from aiogram.dispatcher import FSMContext
# from data.config import CHANNELS
# from loader import dp, bot
#
# @dp.message_handler(commands='register', state=None)
# async def start(message: types.Message):
#     await message.answer("Iltimos raqamingizni kiriting:")
#     await Lists.number.set()
#
# @dp.message_handler(state=Lists.number)
# async def step1(msg: types.Message, state: FSMContext):
#     number = msg.text
#     await state.update_data({'number': number})
#     await msg.answer("Iltimos o'z ism va familiyangizni kiring:")
#     await Lists.parents.set()
#
# @dp.message_handler(state=Lists.parents)
# async def step2(msg: types.Message, state: FSMContext):
#     parents = msg.text
#     await state.update_data({'parents': parents})
#     # await Lists.namesur.set()
#     data = await state.get_data()
#     message = (f"Foydalanuvchining telefon raqami: {data['number']}\n"
#                f"Foydalanuvchining o'z ism va familiyasi: {data['parents']}\n")
#     await bot.send_message(chat_id=CHANNELS[0], text=message)
#     await msg.answer("Xabaringiz qabul qilindi, tashakkur!\n\n"
#     "Siz bilan yaqin orada bizning administratorlar aloqaga chiqadi.")
#     await state.finish()


from aiogram import types
from loader import dp, bot

@dp.message_handler(commands='register')
async def start(message: types.Message):
    await message.answer("<b>Founders Language Schoolga</b> ro'yxatdan o'tmoqchimisiz?\n\n"
                         "Unday bo'lsa quyidagi formani to'ldiring:\n"
                         "👉 Havola: https://forms.gle/CGaDRRrS1sU1Vey26\n\n"
                         "Biz sizni markazimizda ko'rishni intizorlik bilan kutamiz!")
