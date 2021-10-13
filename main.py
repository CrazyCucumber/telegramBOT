import telebot

from functions_student import registration, DatabaseEntry
from functions_teacher import data_check

from config import TOKEN
bot = telebot.TeleBot(TOKEN)


keyboard1 = telebot.types.ReplyKeyboardMarkup(True)
keyboard1.row('Студент', 'Преподаватель')


@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, f'Привет, {message.from_user.first_name}!\nВыбери кто ты: студент или преподаватель', reply_markup=keyboard1)


@bot.message_handler(content_types=['text'])
def send_text(message):
    if message.text == 'Студент':
        msg = bot.send_message(message.chat.id, f'{message.from_user.first_name}, пришли мне ФИО, номер группы,\n'
                                                f'номер задания, номер варианта и ссылку на гитхаб в таком виде:\n'
                                                f'Иванов Иван Иванович, 312Б, 3, 4, git_ref')
        bot.register_next_step_handler(msg, student_register)
    elif message.text == 'Преподаватель':
        msg = bot.send_message(message.chat.id, f'{message.from_user.first_name}, 1 - Посмотреть Базу данных \n')
        bot.register_next_step_handler(msg, teacher_next_step)
def student_register(message):
    registration(message)
    DatabaseEntry(message)
def teacher_next_step(message):
    if message.text == '1':
        data_check(message)



if __name__ == '__main__':
     bot.polling(none_stop=True)
