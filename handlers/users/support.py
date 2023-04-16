from aiogram import Bot, types

from aiogram.dispatcher import Dispatcher, FSMContext
from aiogram.dispatcher.filters import Command

from keyboards.default.reply import get_lang_for_button, get_lang_for_button, changelang
from keyboards.inline.support import  yesno
from states.state import answer
from aiogram.utils import executor


from loader import dp, bot


import sqlite3
# from fuzzywuzzy import fuzz

from translation import _


# def recognize_question(question,questions):
#     recognized={'id':'','percent':0}
#     for key, value in questions.items():
#         for q in value:
#             percent=fuzz.ratio(question,q)
#             if percent>recognized['percent']:
#                 recognized['id']=key
#                 recognized['percent']=percent
#     return recognized['id']

class Database:
    def __init__(self,db_file):
        self.conn = sqlite3.connect(db_file)
        self.cursor = self.conn.cursor()

    def get_questions(self):
        with self.conn:
            result=self.cursor.execute("SELECT id,questions FROM support;",()).fetchall()
            data={}

            for row in result:
                questions=tuple(row[1].split(":"))
                data[row[0]]=questions
            return data

    def get_answer(self,answer_id):
        with self.conn:
            return self.cursor.execute("SELECT answer from support WHERE id=?",(answer_id,)).fetchone()[0]
    def user_exists(self,user_id):
        with self.conn:
            result=self.cursor.execute("SELECT * FROM users where user_id=?",(user_id,)).fetchall()
            return bool(len(result))
    def add_user(self,user_id,lang):
        with self.conn:
            return self.cursor.execute("INSERT INTO users (user_id,lang) VALUES (?, ?)",(user_id,lang))

    def get_lang(self,user_id):
        with self.conn:
            return self.cursor.execute("SELECT lang FROM users WHERE user_id=?",(user_id,)).fetchone()[0]







db = Database('databaseprotestim.db')

# @dp.message_handler(state=answer.A1)
# async def echo_message(msg: types.Message, state: FSMContext):
#     lang = db.get_lang(msg.from_user.id)
#     try:
#         answer_id = recognize_question(msg.text,db.get_questions())
#         # await bot.send_message(msg.from_user.id, answer_id)
#         await bot.send_message(msg.from_user.id, text=f"{db.get_answer(answer_id)}")
#         await bot.send_message(msg.from_user.id, _("Javob sizni qoniqtirdimi",lang), reply_markup=yesno(msg,msg.from_user.id))
#         await bot.send_message(msg.from_user.id, _("Tilni o'zgartirish",lang), reply_markup=changelang())
#
#     except:
#         await bot.send_message(msg.from_user.id, _("Javob sizni qoniqtirdimi",lang), reply_markup=yesno(msg,msg.from_user.id))
#
#     await state.finish()
# @dp.callback_query_handler(text='Ha')
# async def set_lang(call: types.CallbackQuery):
#     lang = db.get_lang(call.from_user.id)
#     await bot.delete_message(call.from_user.id,call.message.message_id)
#
#     await bot.send_message(call.from_user.id,_('Xizmatimizdan foydalananangiz uchun rahmat\n/start - Savolni yuborish uchun,'
#                                                '/help - Biz haqimizda',lang))
#     await bot.send_message(call.message.from_user.id, _("Tilni o'zgartirish", lang), reply_markup=changelang())

