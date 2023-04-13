from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Command
from aiogram.types import ReplyKeyboardRemove
from aiogram.utils import callback_data

from data.config import support_ids
from db import db
from keyboards.inline.support import support_keyboard, support_callback, langMenu, cancel_support_callback
from loader import dp, bot
from states.state import questions, RegistrationStates
from translation import _

cb_data = callback_data.CallbackData("/ask", "param1", "param2")

# Define a callback query handler
@dp.message_handler(Command("ask"))
async def ask_support(message: types.Message):
    if not db.user_exists(message.from_user.id):
        await bot.send_message(message.from_user.id, 'Assalomu aleykum, Protestim  yordamchi botiga hush kelibsiz! ')
        await bot.send_message(message.from_user.id, 'Tilni tanlang: ', reply_markup=langMenu)
        await RegistrationStates.lang.set()
    else:
        lang = db.get_lang(message.from_user.id)

        text = _("Texnik yordam bilan bog'lanmoqchimisiz? Quyidagi tugmani bosing", lang)
        keyboard = await support_keyboard(message, messages="one")
        await message.answer(text, reply_markup=keyboard)

@dp.callback_query_handler(support_callback.filter(messages="one"))
async def send_to_support(call: types.CallbackQuery, state: FSMContext, callback_data: dict):

    await call.answer()
    user_id = int(callback_data.get("user_id"))
    lang = db.get_lang(call.from_user.id)

    await call.message.answer(_("Siz yubormoqchi bo'lgan savolingizni to'liq shaklda yuboring",lang))

    await state.set_state("wait_for_support_message")
    await state.update_data(second_id=user_id)


@dp.message_handler(state="wait_for_support_message", content_types=types.ContentTypes.ANY)
async def get_support_message(message: types.Message, state: FSMContext):
    lang = db.get_lang(message.from_user.id)
    await message.answer(_('sizni savolingiz bizning operatorlarga yuborildi yaqin orada sizga javob beramiz',lang))
    data = await state.get_data()
    second_id = data.get("second_id")
    name=db.get_name(message.from_user.id)
    phone=db.get_phone(message.from_user.id)

    for support_id in support_ids:
        if str(second_id)==support_id:

            lang = db.get_lang(message.from_user.id)
            # await bot.send_message(second_id,f"Sizga {str(name)} userdan xat \n@{message.from_user.username}\n nomeri {phone}\n")
            keyboard = await support_keyboard(message,messages="one", user_id=message.from_user.id)
            db.add_questions(message.from_user.id,message.text)

            # try:
            #     reply = db.get_question(second_id)
            #     await bot.send_message(second_id,f"Sizni <code>{reply}</code> ushbu savolingizga javob berildi")
            # except Exception:
            #     print('')
            await bot.send_message(second_id,f"Sizga {str(name)} userdan xat \n telegramdagi accaunti @{message.from_user.username}\n nomeri {phone}\nSavol {message.text}", reply_markup=keyboard)



            await bot.send_message(-1001712239399,
                                   f"Sizga {str(name)} userdan xat \n telegramdagi accaunti@{message.from_user.username}\n nomeri {phone}\nSavol {message.text}")

        else:

            lang = db.get_lang(message.from_user.id)
            db.add_questions(message.from_user.id, message.text)

            try:
                reply = db.get_question(second_id)
                await bot.send_message(second_id, _(f"Sizni <code>{reply}</code> ushbu savolingizga javob berildi",lang))

            except Exception:
                print('')

            keyboard = await support_keyboard(message,messages="one", user_id=message.from_user.id)
            await message.copy_to(second_id)
            await bot.send_message(second_id,_("Yana savol bolsa /ask buyrugini ishlating",lang))
    await state.reset_state()
@dp.callback_query_handler(cancel_support_callback.filter(), state=["in_support", "wait_in_support", None])
async def exit_support(call: types.CallbackQuery, state: FSMContext, callback_data: dict):
    user_id = int(callback_data.get("user_id"))
    second_state = dp.current_state(user=user_id, chat=user_id)

    if await second_state.get_state() is not None:
        data_second = await second_state.get_data()
        second_id = data_second.get("second_id")
        if int(second_id) == call.from_user.id:
            await second_state.reset_state()
            await bot.send_message(user_id, "Пользователь завершил сеанс техподдержки")

    await call.message.answer("Protestim bu sizni  bilimingzini ssinash uchun qilingan platforma")
    await state.reset_state()