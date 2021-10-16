import telebot
import psycopg2
from psycopg2 import Error

from functions_github import download_rep

from env import *

bot = telebot.TeleBot(bot_token)


def database_entry(all_message):
    global cur, con
    try:
        con = psycopg2.connect(
            database=db_name,
            user=db_user,
            password=db_password,
            host=db_host,
            port=db_port,
        )
        logger.debug("Connection with PostgreSQL established")
        fam = all_message[0]
        name = all_message[1]
        patronymic = all_message[2]
        grp = all_message[3]
        task = all_message[4]
        var = all_message[5]
        git = all_message[6]
        sql_query_to_entry_student = f"INSERT INTO student (fam,name,patronymic,grp,task,var,git, process) VALUES" \
                                     f" ('{fam}','{name}', '{patronymic}', '{grp}', '{task}', '{var}', '{git}'," \
                                     f" '{download_rep(git)}')"

        cur = con.cursor()
        cur.execute(sql_query_to_entry_student)
        con.commit()
        logger.debug("Student recorded in PostgreSQL")
    except (Exception, Error) as error:
        logger.error("Error while working with PostgreSQL", error)
    finally:
        if cur:
            cur.close()
            con.close()
            logger.debug("PostgreSQL connection closed")
