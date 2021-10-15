import telebot
import psycopg2
from config import TOKEN

bot = telebot.TeleBot(TOKEN)

con = psycopg2.connect(
    database="mai",
    user="postgres",
    password="1324",
    host="127.0.0.1",
    port="5432",
)


def data_check(message):
    sql_query_to_check_all_students = 'SELECT * FROM student;'

    cur = con.cursor()
    data = cur.execute(sql_query_to_check_all_students)
    con.commit()
    bot.send_message(message.chat.id, data)
    con.close()
