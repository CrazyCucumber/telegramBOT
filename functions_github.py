import telebot
import os
import shutil

from functions_student import registration

from config import TOKEN

bot = telebot.TeleBot(TOKEN)


def download_rep(message):
    git = registration(message)[6]
    global new_dir
    try:
        os.chdir('..')
        dir_now = os.getcwd()
        new_dir = os.path.join(dir_now, 'NewDirForProgram')
        os.mkdir(new_dir)
    except FileExistsError:
        shutil.rmtree(new_dir, ignore_errors=True)
        os.mkdir(new_dir)
    os.chdir(new_dir)
    os.system(f'git clone {git}')
    os.system('git init\n'
              'git add .\n'
              'git commit -m "Add files from new rep"\n'
              'git push -f origin main')
