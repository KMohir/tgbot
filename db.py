
import sqlite3

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
    def add_questions(self,userid,question):
        with self.conn:
            return self.cursor.execute("INSERT INTO userquestions (userid,question) VALUES (?,?)",(userid,question))

    def get_question(self, answer_id):
        with self.conn:
            return self.cursor.execute("SELECT question from userquestions WHERE userid=?",
                                       (answer_id,)).fetchall()[-1][0]
    def question(self,answer_id):
        with self.conn:
            return self.cursor.execute("SELECT question from userquestions WHERE id=?",(answer_id,)).fetchone()
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
    def change_lang(self,user_id,languege):
        with self.conn:
            return self.cursor.execute("UPDATE users SET lang = ? WHERE user_id=?",(languege,user_id))
    def update(self,lang,user_id,name,phone):
        with self.conn:
            return self.cursor.execute("INSERT INTO users(user_id,lang,name,phone) VALUES (?,?,?,?)",(user_id,lang,name,phone))
    def get_name(self,user_id):
        with self.conn:
            return self.cursor.execute("SELECT name FROM users WHERE user_id=?",(user_id,)).fetchone()[0]
    def get_phone(self,user_id):
        with self.conn:
            return self.cursor.execute("SELECT phone FROM users WHERE user_id=?",(user_id,)).fetchone()[0]

db=Database('databaseprotestim.db')