from loader import dp
from aiogram import types

@dp.message_handler(commands=['aboutus'])
async def about_us(message: types.Message):
    text = ("🔥 O'zbekistondagi eng tezkor o'quv markaziga xush kelibsiz!\n\n"
        "Biz sizga kafolat va sifatni va'da qilamiz.\n\n"
        "💥 O'quv markazimizda siz tekin coworking zonalari, Free Wi-Fi, darsliklar bilan ta'minlanasiz.\n\n"
        "Ha aytgancha har yakshanba o'smirlar va bolalar uchun bo'lib o'tadigan speaking clublar, ajoyib eventlar va MOCK examlar sizni kutib qoladi.\n\n"
        "Qulay fursatni boy bermaslik uchun /register buyrug'ini bering!\n\n"
        "😉 Operatorlarimiz siz bilan yaqin fursatlarda bog'lanadi.\n\n")

    await message.answer(text)
