import telebot
import psycopg2
from functions_student import registration
from config import TOKEN
bot = telebot.TeleBot(TOKEN)


con = psycopg2.connect(
  database="mai",
  user="postgres",
  password="1324",
  host="127.0.0.1",
  port="5432"
)


def DatabaseEntry(message):

  #Подготовка SQL запроса
  fam = "\'" + registration(message)[0] + "\'"
  name = "\'" + registration(message)[1] + "\'"
  otchestvo = "\'" + registration(message)[2] + "\'"
  group = "\'" + registration(message)[3] + "\'"
  git = "\'" + registration(message)[6] + "\'"
  SQLquery_to_entry_student = f"INSERT INTO STUDENT (fam,name,otchestvo,group,task, var, git) VALUES ({fam}, {name}, {otchestvo}," \
             f" {group}, {registration(message)[4]}, {registration(message)[5]}, {git})"
  SQLquery_to_create_database = '''CREATE TABLE student (
             id BIGSERIAL NOT NULL PRIMARY KEY,
             fam VARCHAR(50),
             name VARCHAR(50),
             otchestvo VARCHAR(50),
             group VARCHAR(50),
             task INT NOT NULL,
             var INT NOT NULL,
             git VARCHAR(200));'''

  cur = con.cursor()

  try:
    cur.execute(SQLquery_to_create_database)
  except psycopg2.errors.DuplicateTable:
    pass
  finally:
    cur.execute(SQLquery_to_entry_student)
    con.commit()
    con.close()

  return bot.send_message(message.chat.id, f'{message.from_user.first_name}, Вы записаны в Базу Данных')

