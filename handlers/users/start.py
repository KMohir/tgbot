from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.builtin import CommandStart
from aiogram.types import ParseMode, Message, ReplyKeyboardRemove

from db import db
from keyboards.default.reply import key
from keyboards.inline.support import langMenu, support_keyboard
from loader import dp, bot

# from keyboards.default.reply import get_lang_for_button, get_project_for_user
from states.state import answer, RegistrationStates, questions
from translation import _

global lang
@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):

    if not db.user_exists(message.from_user.id):
        await bot.send_message(message.from_user.id,'Assalomu aleykum, Protestim  yordamchi botiga hush kelibsiz! ')
        await bot.send_message(message.from_user.id,'Tilni tanlang: ',reply_markup=langMenu)
        await RegistrationStates.lang.set()
    else:
        try:
            lang = db.get_lang(message.from_user.id)
            await bot.send_message(message.from_user.id, _('Operator bilan /ask ni bosip boglansez boladi',lang),reply_markup=ReplyKeyboardRemove())
        except:
            await bot.send_message(message.from_user.id, 'Operator bilan /ask ni bosip boglansez boladi',
                                   reply_markup=ReplyKeyboardRemove())
    # else:
    #     lang=db.get_lang(message.from_user.id)
    #
    #     text = _("Texnik yordam bilan bog'lanmoqchimisiz? Quyidagi tugmani bosing", lang)
    #     keyboard = await support_keyboard(message, messages="one")
    #     await message.answer(text, reply_markup=keyboard)






@dp.callback_query_handler(text_contains="lang_",state=RegistrationStates.lang)
async def set_lang(call: types.CallbackQuery, state: FSMContext):

    if not db.user_exists(call.from_user.id):

        lang=call.data[5:]
        async with state.proxy() as data:

            data['lang'] = lang


        if lang =='uz':
            await bot.send_message(call.from_user.id,"Ismingizni kiriting")
        elif lang =='ru':
            await bot.send_message(call.from_user.id, "Введите свое имя")


        await RegistrationStates.name.set()



@dp.message_handler(state=RegistrationStates.name)
async def register_command_handler(message: types.Message, state: FSMContext):
    name=message.text
    data = await state.get_data()

    lang=data.get('lang')
    async with state.proxy() as data:

        data['name'] = name
    if lang=="uz":
        await message.answer("Raqamingizni yuborish uchun pastdagi tugmani bosing",reply_markup=key(lang))
    elif lang=="ru":
        await message.answer("Нажмите кнопку ниже, чтобы отправить свой номер", reply_markup=key(lang))
    await RegistrationStates.end.set()

# Name handler

# Phone handler



@dp.message_handler(state=RegistrationStates.end, content_types=types.ContentType.CONTACT)
async def process_name(message: Message, state: FSMContext):

    data = await state.get_data()
    name = data.get('name')
    lan=data.get('lang')
    contact = message.contact.phone_number
    data = await state.get_data()
    db.update(lan,message.from_user.id,name,contact)
    lang = db.get_lang(message.from_user.id)
    await message.answer(_("Ro'yxatdan o'tdingiz",lang), reply_markup=ReplyKeyboardRemove())
    text = _("Texnik yordam bilan bog'lanmoqchimisiz? Quyidagi tugmani bosing", lang)
    keyboard = await support_keyboard(message, messages="one")
    await message.answer(text, reply_markup=keyboard)
    await state.finish()




