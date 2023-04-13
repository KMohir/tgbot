from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandHelp

from loader import dp


@dp.message_handler(CommandHelp())
async def bot_help(message: types.Message):
    text = ("/ask - Savol yuborish",
            "/help - botni ishlatish")
    
    await message.answer("\n".join(text))
