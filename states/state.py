from aiogram.dispatcher.filters.state import StatesGroup, State


class answer(StatesGroup):
    A1 = State()
    A2 = State()

class language(StatesGroup):
    lang = State()

class questions(StatesGroup):
    answer = State()
class RegistrationStates(StatesGroup):
    lang=State()
    name = State()
    phone = State()
    end = State()
    number=State()
    help = State()
