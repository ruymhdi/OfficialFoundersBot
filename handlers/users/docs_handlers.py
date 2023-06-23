from loader import dp, bot
from aiogram.types import ContentType, Message


@dp.message_handler()
async def text_handler(message: Message):
    await message.reply('Siz matn yubordingiz!')

@dp.message_handler(content_types=ContentType.VIDEO)
async def doc_handler(message: Message):
    await message.video.download()
    await message.reply("Video qabul yubordingiz!\n"
                        f"file_id = {message.video.file_id}")
