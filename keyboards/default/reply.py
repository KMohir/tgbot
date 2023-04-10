from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

from db import db
from translation import _


def get_lang_for_button(message):
    lang = db.get_lang(message.from_user.id)
    button=ReplyKeyboardMarkup(
        keyboard=[
            [
                KeyboardButton(text=_("Texnik yordamga xabar yozish",lang)
    )
            ],
            [
                KeyboardButton(text=_("Texnik yordam bilan suhbatlashish",lang))
            ],

        ],
        resize_keyboard=True
    )
    return button
# def get_project_for_user(message):
#     lang = db.get_lang(message.from_user.id)
#     button=ReplyKeyboardMarkup(
#         keyboard=[
#             [
#                 KeyboardButton(text=_("Protestim",lang)
#     )
#             ],
#             [
#                 KeyboardButton(text=_("2 chi proyekt",lang))
#             ],
#             [
#                 KeyboardButton(text=_("3 chi proyekt",lang)
#     )
#             ],
#             [
#                 KeyboardButton(text=_("4 chi proyekt",lang))
#             ],
#
#         ],
#         resize_keyboard=True
#     )
#     return button

def get_lang_for_button1(message):
    lang = db.get_lang(message.from_user.id)
    button=ReplyKeyboardMarkup(
        keyboard=[

            [
                KeyboardButton(text=_("Texnik yordam bilan suhbatlashish",lang))
            ],

        ],
        resize_keyboard=True
    )
    return button

def change_lang():

    button=ReplyKeyboardMarkup(
        keyboard=[
            [
                KeyboardButton(text="Русский язык")

            ],
            [
                KeyboardButton(text="O'zbek tili")
            ],

        ],
        resize_keyboard=True
    )
    return button
def changelang():

    button=ReplyKeyboardMarkup(
        keyboard=[
            [
                KeyboardButton(text="Tilni o'zgartirish")

            ],

        ],
        resize_keyboard=True
    )
    return button
def key(lang):
    if lang=='uz':
        keyboardcontakt=ReplyKeyboardMarkup(

            keyboard=[[

                KeyboardButton(text="Agar raqamingizni yubormoqchi bo'lsangiz, ustiga bosing",
                               request_contact=True

                               )
                ],

            ],resize_keyboard=True

        )
    elif lang=='ru':
        keyboardcontakt=ReplyKeyboardMarkup(

            keyboard=[[

                KeyboardButton(text="Нажмите на это, если хотите отправить свой номер",
                               request_contact=True

                               )
                ],

            ],resize_keyboard=True

        )
    return keyboardcontakt