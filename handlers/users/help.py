from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.builtin import CommandHelp, Command
from aiogram.types import ReplyKeyboardRemove

from db import db
from loader import dp
from states.state import RegistrationStates
from translation import _


@dp.message_handler(state=RegistrationStates.help)
@dp.message_handler(Command("help"))
async def bot_help(message: types.Message,state:FSMContext):
    lang = db.get_lang(message.from_user.id)
    text = (_("Buyruqlar ro'yxati:\n/ask - Texnik yordamga habar yozish\n/change_language - Tilni o'zgartish\n/about - ProTestim haqida bilish", lang))

    
    await message.answer(text,reply_markup=ReplyKeyboardRemove())
    await state.finish()




