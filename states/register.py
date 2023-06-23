from aiogram.dispatcher.filters.state import StatesGroup, State

class Lists(StatesGroup):
    name_surname = State()
    contact = State()

class Medias(StatesGroup):
    kidsvideo = State()
    generalvideo = State()
    iltesturbo = State()