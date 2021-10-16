import telebot

from functions_student import registration

from env import bot_token

bot = telebot.TeleBot(bot_token)


@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, f'{message.from_user.first_name}, пришли мне ФИО, номер группы,\n'
                                      f'номер задания, номер варианта и ссылку на гитхаб в таком виде:\n'
                                      f'Иванов Иван Иванович, 312Б, 3, 4, git_ref')


@bot.message_handler(content_types=['text'])
def student_register(message):
    bot.register_next_step_handler(registration(message), student_register)


if __name__ == '__main__':
    bot.polling(none_stop=True)
