from aiogram import types


async def set_default_commands(dp):
    await dp.bot.set_my_commands(
        [
            types.BotCommand("start", "Botni ishga tushurish"),
            types.BotCommand("help", "Yordam"),
            types.BotCommand("aboutus", "Biz haqimizda"),
            types.BotCommand("aboutadresses", "Bizning manzillar"),
            types.BotCommand("ieltsturbo", "IELTS Turbo"),
            types.BotCommand("kidsenglish", "KIDS English"),
            types.BotCommand("generalenglish", "General English"),
            types.BotCommand("register", "Registratsiyadan o'tish"),
        ]
    )
