import telebot
import psycopg2

from functions_student import registration
from functions_github import download_rep

from config import TOKEN

bot = telebot.TeleBot(TOKEN)

con = psycopg2.connect(
    database="mai",
    user="postgres",
    password="1324",
    host="127.0.0.1",
    port="5432",
)


def database_entry(message):
    fam = "\'" + registration(message)[0] + "\'"
    name = "\'" + registration(message)[1] + "\'"
    patronymic = "\'" + registration(message)[2] + "\'"
    grp = "\'" + registration(message)[3] + "\'"
    git = "\'" + registration(message)[6] + "\'"
    sql_query_to_entry_student = f"INSERT INTO student (fam,name,patronymic,grp,task,var,git, process) VALUES ({fam}," \
                                 f" {name}, {patronymic}, {grp}, {registration(message)[4]}," \
                                 f" {registration(message)[5]}, {git}, {download_rep(message)})"

    cur = con.cursor()
    cur.execute(sql_query_to_entry_student)
    con.commit()
    con.close()

    return bot.send_message(message.chat.id, f'{message.from_user.first_name}, Вы записаны в Базу Данных')
