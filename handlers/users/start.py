from aiogram.types import ContentTypes
from states.register import Lists
from aiogram.dispatcher import FSMContext
from aiogram.types import ReplyKeyboardRemove
from aiogram import types
from loader import dp, bot
from handlers.users.help import bot_help


@dp.message_handler(commands='start', state=None)
async def start_command(message: types.Message, state: FSMContext):
    await bot.send_message(chat_id=message.chat.id, text="Iltimos ism va familiyangizni kiriting.")
    await Lists.name_surname.set()


@dp.message_handler(state=Lists.name_surname)
async def process_name(message: types.Message, state: FSMContext):
    name = message.text
    await state.update_data(name=name)

    await bot.send_message(chat_id=message.chat.id, text="Iltimos kontaktingizni yuboring!", reply_markup=types.ReplyKeyboardMarkup(
        keyboard=[
            [
                types.KeyboardButton(text="📱 Kontaktni yuborish", request_contact=True)
            ]
        ],
        resize_keyboard=True
    ))
    await Lists.contact.set()


@dp.message_handler(content_types=ContentTypes.CONTACT, state=Lists.contact)
async def process_contact(message: types.Message, state: FSMContext):
    contact_info = message.contact
    state_data = await state.get_data()
    name = state_data['name']

    await bot.send_message(chat_id=message.chat.id, text="Sizning kontaktingiz qabul qilindi.",
                           reply_markup=ReplyKeyboardRemove())

    xabar = f"<b>Foydalanuchi ismi</b>: {name}\n" \
            f"<b>Contact info</b>: {contact_info.phone_number}\n"

    await bot.send_message(chat_id='-1001829161444', text=f"{xabar}")
    await state.finish()


@dp.message_handler()
async def handle_all_messages(message: types.Message):
    await bot.send_message(chat_id=message.chat.id, text="Sizning komandangizni tushundmadim.\n\n"
                                                         "Iltimos agar registratisyadan o'tmoqchi bo'lsangiz /help buyrug'ini bering.")
