from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.types import ReplyKeyboardRemove

from db import db
from loader import dp
from keyboards.default.reply import get_lang_for_button, change_lang
from states.state import answer, language
from translation import _


@dp.message_handler(text="/change_language")
async def bot_echo(message: types.Message):
    lang=db.get_lang(message.from_user.id)
    await message.answer(_('Tilni tanlang',lang),reply_markup=change_lang())
    await language.lang.set()
@dp.message_handler(state=language.lang)
async def bot_echo(message: types.Message,state: FSMContext):
    if message.text == "O'zbek tili":
        db.change_lang(message.from_user.id, 'uz')
        await message.answer("Til o'zbek tiliga o'zgartirildi",reply_markup=ReplyKeyboardRemove())
    if message.text == "Русский язык":
        db.change_lang(message.from_user.id, 'ru')
        await message.answer("Язык изменился на русском",reply_markup=ReplyKeyboardRemove())
    await state.finish()
# Эхо хендлер, куда летят текстовые сообщения без указанного состояния
@dp.message_handler(state=None)
async def bot_echo(message: types.Message):
    lang=db.get_lang(message.from_user.id)
    await message.answer(_('Yuqoridagi tugmalardan birini tanlang',lang))


# Эхо хендлер, куда летят ВСЕ сообщения с указанным состоянием
@dp.message_handler(state="*", content_types=types.ContentTypes.ANY)
async def bot_echo_all(message: types.Message, state: FSMContext):
    state = await state.get_state()
    try:
        lang=db.get_lang(message.from_user.id)
        await message.answer(_('Pastdagi tugmani bosing tugmani bosing',lang))
    except Exception as e:

        await message.answer('Tugmani bosing')
    # await message.answer(f"Эхо в состоянии <code>{state}</code>.\n"
    #                      f"\nСодержание сообщения:\n"
    #                      f"<code>{message}</code>")
