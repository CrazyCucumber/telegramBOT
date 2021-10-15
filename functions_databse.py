import telebot
import psycopg2
from psycopg2 import Error


from functions_github import download_rep

from config import TOKEN

bot = telebot.TeleBot(TOKEN)

# con = psycopg2.connect(
#     database="mai",
#     user="postgres",
#     password="1324",
#     host="127.0.0.1",
#     port="5432",
# )


def database_entry(all_message):
    # fam = "\'" + registration(message)[0] + "\'"
    # name = "\'" + registration(message)[1] + "\'"
    # patronymic = "\'" + registration(message)[2] + "\'"
    # grp = "\'" + registration(message)[3] + "\'"
    # git = "\'" + registration(message)[6] + "\'"
    # fam = all_message[0]
    # name = all_message[1]
    # patronymic = all_message[2]
    # grp = all_message[3]
    # task = all_message[4]
    # var = all_message[5]
    # git = all_message[6]
    # sql_query_to_entry_student = f"INSERT INTO student (fam,name,patronymic,grp,task,var,git, process) VALUES ('{fam}'," \
    #                              f" '{name}', '{patronymic}', '{grp}', '{task}', '{var}', '{git}', '{download_rep(git)}')"
    #
    # cur = con.cursor()
    # cur.execute(sql_query_to_entry_student)
    # con.commit()
    # con.close()
    global cur
    try:
        con = psycopg2.connect(
            database="mai",
            user="postgres",
            password="1324",
            host="127.0.0.1",
            port="5432",
        )
        fam = all_message[0]
        name = all_message[1]
        patronymic = all_message[2]
        grp = all_message[3]
        task = all_message[4]
        var = all_message[5]
        git = all_message[6]
        sql_query_to_entry_student = f"INSERT INTO student (fam,name,patronymic,grp,task,var,git, process) VALUES ('{fam}'," \
                                     f" '{name}', '{patronymic}', '{grp}', '{task}', '{var}', '{git}', '{download_rep(git)}')"

        cur = con.cursor()
        cur.execute(sql_query_to_entry_student)
        con.commit()
        con.close()
    except (Exception, Error) as error:
        print("Ошибка при работе с PostgreSQL", error)
    finally:
        if con:
            cur.close()
            con.close()
            print("Соединение с PostgreSQL закрыто")
