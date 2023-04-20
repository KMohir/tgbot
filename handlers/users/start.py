from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.builtin import CommandStart
from aiogram.types import ParseMode, Message, ReplyKeyboardRemove

from db import db
from keyboards.default.reply import key, get_lang_for_button
from keyboards.inline.support import langMenu, support_keyboard
from loader import dp, bot

# from keyboards.default.reply import get_lang_for_button, get_project_for_user
from states.state import answer, RegistrationStates, questions
from translation import _

global lang
@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):

    if not db.user_exists(message.from_user.id):
        await bot.send_message(message.from_user.id,'Assalomu aleykum, ProTestim yordamchi botiga hush kelibsiz!\nЗдраствуйте, добро пожаловать в бот поддержки ProTestim!')
        await bot.send_message(message.from_user.id,'Tilni tanlang:\nВыберите язык:',reply_markup=langMenu)
        await RegistrationStates.lang.set()
    else:

        try:

            lang = db.get_lang(message.from_user.id)
            text = (_("Buyruqlar ro'yxati:\n/ask - Texnik yordamga habar yozish\n/change_language - Tilni o'zgartish\n/about - ProTestim haqida bilish", lang),get_lang_for_button(message))
            await bot.send_message(message.from_user.id,text,reply_markup=ReplyKeyboardRemove())
        except:
            await bot.send_message(message.from_user.id, "Buyruqlar ro'yxati:\n/ask - Texnik yordamga habar yozish\n/change_language - Tilni o'zgartish\n/about - ProTestim haqida bilish",
                                   reply_markup=get_lang_for_button(message))
    # else:
    #     lang=db.get_lang(message.from_user.id)
    #
    #     text = _("Texnik yordam bilan bog'lanmoqchimisiz? Quyidagi tugmani bosing", lang)
    #     keyboard = await support_keyboard(message, messages="one")
    #     await message.answer(text, reply_markup=keyboard)






@dp.callback_query_handler(text_contains="lang_",state=RegistrationStates.lang)
async def set_lang(call: types.CallbackQuery, state: FSMContext):
    await call.answer()
    if not db.user_exists(call.from_user.id):

        lang=call.data[5:]
        async with state.proxy() as data:

            data['lang'] = lang


        if lang =='uz':
            await bot.send_message(call.from_user.id,"Ism familiyangizni kiriting")
        elif lang =='ru':
            await bot.send_message(call.from_user.id, "Введите свое имя и фамилию")


        await RegistrationStates.name.set()



@dp.message_handler(state=RegistrationStates.name)
async def register_command_handler(message: types.Message, state: FSMContext):
    name=message.text
    data = await state.get_data()

    lang=data.get('lang')
    async with state.proxy() as data:

        data['name'] = name
    if lang=="uz":
        await message.answer("Telefon raqamingizni kiriting",reply_markup=key(lang))
    elif lang=="ru":
        await message.answer("Введите свой номер телефона",reply_markup=key(lang))
    await RegistrationStates.end.set()

# Name handler

# Phone handler

@dp.message_handler(state=RegistrationStates.end, content_types=types.ContentType.TEXT)
async def process_name(message: Message, state: FSMContext):
    data = await state.get_data()
    lang=data.get('lang')
    contact =message.text
    if contact[0:4]=='+998':
        data = await state.get_data()
        name = data.get('name')
        lan=data.get('lang')
        # contact = message.contact.phone_number
        data = await state.get_data()
        db.update(lan,message.from_user.id,name,contact)
        lang = db.get_lang(message.from_user.id)
        await message.answer(_("Ro'yxatdan muvaffaqiyatli o'tdingiz!",lang), reply_markup=ReplyKeyboardRemove())


        lang = db.get_lang(message.from_user.id)
        text = (
            _("Buyruqlar ro'yxati:\n/ask - Texnik yordamga habar yozish\n/change_language - Tilni o'zgartish\n/about - ProTestim haqida bilish",
              lang))

        await message.answer(text, reply_markup=get_lang_for_button(message))
        await state.finish()
    else:
        await message.answer(_("Telefon raqam noto'g'ri kiritildi, iltimos telefon raqamni +998XXXXXXXX formatda kiriting yoki 'Kontakni yuborish' tugmasiga bosing.",lang),reply_markup=key(lang))
        await RegistrationStates.end.set()


@dp.message_handler(state=RegistrationStates.end, content_types=types.ContentType.CONTACT)
async def process_name(message: Message, state: FSMContext):

    data = await state.get_data()
    name = data.get('name')
    lan=data.get('lang')
    contact = message.contact.phone_number
    data = await state.get_data()
    db.update(lan,message.from_user.id,name,contact)
    lang = db.get_lang(message.from_user.id)
    await message.answer(_("Ro'yxatdan muvaffaqiyatli o'tdingiz!",lang), reply_markup=ReplyKeyboardRemove())


    lang = db.get_lang(message.from_user.id)
    text = (
        _("Buyruqlar ro'yxati:\n/ask - Texnik yordamga habar yozish\n/change_language - Tilni o'zgartish\n/about - ProTestim haqida bilish",
          lang))

    await message.answer(text, reply_markup=get_lang_for_button(message))
    await state.finish()







