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
@dp.message_handler(text="Написать в техническую поддержку")
@dp.message_handler(text="Texnik yordamga habar yozish")
async def ask_support(message: types.Message, state: FSMContext):
    if not db.user_exists(message.from_user.id):
        await bot.send_message(message.from_user.id, 'Assalomu aleykum, Protestim  yordamchi botiga hush kelibsiz! ')
        await bot.send_message(message.from_user.id, 'Tilni tanlang: ', reply_markup=langMenu)
        await RegistrationStates.lang.set()
    else:
        lang = db.get_lang(message.from_user.id)

        user_id = 5657091547
        lang = db.get_lang(message.from_user.id)

        try:

            await message.answer(_("Savolingizni yoki murojatingizni 1 ta habar orqali yuboring.", lang))
        except Exception as ex:
            await message.answer(_("Savolingizni yoki murojatingizni 1 ta habar orqali yuboring.", lang))
        await state.set_state("wait_for_support_message")
        await state.update_data(second_id=user_id)
@dp.callback_query_handler(support_callback.filter(messages="one"))
async def send_to_support(call: types.CallbackQuery, state: FSMContext, callback_data: dict):

    await call.answer()
    user_id = int(callback_data.get("user_id"))



    try:
        lang = db.get_lang(call.from_user.id)
        await call.message.answer(_("Savolingizni yoki murojatingizni 1 ta habar orqali yuboring.",lang))
    except Exception as ex:
        await call.message.answer("Savolingizni yoki murojatingizni 1 ta habar orqali yuboring.")
    await state.set_state("wait_for_support_message")
    await state.update_data(second_id=user_id)


@dp.message_handler(state="wait_for_support_message", content_types=types.ContentTypes.ANY)
async def get_support_message(message: types.Message, state: FSMContext):
    try:
        lang = db.get_lang(message.from_user.id)
        await message.answer(_('Savolingiz / Murojatingiz bizning operatorlarga yuborildi, yaqin orada sizga javob beramiz!',lang))
    except:
        await message.answer('Savolingiz / Murojatingiz bizning operatorlarga yuborildi, yaqin orada sizga javob beramiz!')
    data = await state.get_data()
    second_id = data.get("second_id")
    name=db.get_name(message.from_user.id)
    phone=db.get_phone(message.from_user.id)

    for support_id in support_ids:
        if str(second_id)==support_id:

            lang = db.get_lang(message.from_user.id)
            # await bot.send_message(second_id,f"Sizga {str(name)} userdan xat \n@{message.from_user.username}\n nomeri {phone}\n")
            keyboard = await support_keyboard(message,messages="one", user_id=message.from_user.id)
            db.add_questions(message.from_user.id, message.message_id)
            if message.text==None:
                await message.copy_to(second_id,caption=f"Sizga {str(name)} userdan xat \n telegramdagi accaunti @{message.from_user.username}\n nomeri {phone}\nSavol {message.caption}", reply_markup=keyboard)
            else:
                await bot.send_message(second_id,
                                       f"Sizga {str(name)} userdan xat \n telegramdagi accaunti @{message.from_user.username}\n nomeri <code>{phone}</code>\nSavol {message.text}",
                                       reply_markup=keyboard)
            if message.text==None:
                await message.copy_to(-1001712239399,caption=f"Sizga {str(name)} userdan xat \n telegramdagi accaunti @{message.from_user.username}\n nomeri <code>{phone}</code>\nSavol {message.caption}", reply_markup=keyboard)
            else:
                await bot.send_message(-1001712239399,
                                       f"Sizga {str(name)} userdan xat \n telegramdagi accaunti @{message.from_user.username}\n nomeri {phone}\nSavol {message.text}")
            # try:
            #     reply = db.get_question(second_id)
            #     await bot.send_message(second_id,f"Sizni <code>{reply}</code> ushbu savolingizga javob berildi")
            # except Exception:
            #     print('')





        else:


            db.add_questions(message.from_user.id, message.message_id)
            reply = db.get_question(second_id)
            keyboard = await support_keyboard(message,messages="one", user_id=message.from_user.id)
            try:
                await message.copy_to(second_id, reply_to_message_id=reply,
                                          caption=message.caption)
            except Exception:
                print('')
            lang = db.get_lang(second_id)

            await bot.send_message(second_id,_("Yana savolingiz yoki murojatingiz bo'lsa, /ask orqali berishingiz mumkin.",lang))
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

@dp.message_handler(Command("about"))
@dp.message_handler(text="ProTestim haqida bilish")
@dp.message_handler(text="Узнать про ProTestim")
async def bot_help(message: types.Message):
    try:
        lang = db.get_lang(message.from_user.id)
        text = (_("ProTestim - DTM imtihon simulyator platformasi bo'lib, unda havfsiz va hohlagan marobata test topshirib, quyidagi ma'lumotlarga ega bo'ling:\n1. Oliy Ta'lim muassasalarining reytingi\n2. Siz kirmoqchi bo'lgan Ta'lim Muassasasiga qanchalik tayyor ekanligizni\n3. Hozirgi bilimingiz darajasi\n4. Bilimingiz darajasi bilan qaysi Ta'lim Muassasalariga Grant yoki Kontrakt asosida kirishingizni\n5. Qaysi fanda yoki yo'nalishda bilimingizni kuchaytirish kerak ekanligini", lang))
    except Exception as e:
        text = ("ProTestim - DTM imtihon simulyator platformasi bo'lib, unda havfsiz va hohlagan marobata test topshirib, quyidagi ma'lumotlarga ega bo'ling:\n1. Oliy Ta'lim muassasalarining reytingi\n2. Siz kirmoqchi bo'lgan Ta'lim Muassasasiga qanchalik tayyor ekanligizni\n3. Hozirgi bilimingiz darajasi\n4. Bilimingiz darajasi bilan qaysi Ta'lim Muassasalariga Grant yoki Kontrakt asosida kirishingizni\n5. Qaysi fanda yoki yo'nalishda bilimingizni kuchaytirish kerak ekanligini")
    await message.answer(text)