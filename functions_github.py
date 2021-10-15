import telebot
import os
import shutil

from functions_student import registration

from config import TOKEN

bot = telebot.TeleBot(TOKEN)


def download_rep(message):
    git_student = registration(message)[6]
    git_teacher = 'https://github.com/CrazyCucumber/unit_test.git'
    global new_dir
    try:
        os.chdir('..')
        print(os.getcwd())
        dir_now = os.getcwd()
        print(dir_now)
        new_dir = os.path.join(dir_now, 'NewDirForProgram')
        print(new_dir)
        os.mkdir(new_dir)
    except FileExistsError:
        print('Отловил ошибку')
        shutil.rmtree('./NewDirForProgram')
        new_dir = os.path.join(dir_now, 'NewDirForProgram')
        print(new_dir)
        print(os.getcwd())
        os.mkdir(new_dir)
    finally:
        os.chdir(new_dir)
        print(os.getcwd())
    # os.chdir('..')
    # dir_now = os.getcwd()
    # new_dir = os.path.join(dir_now, 'NewDirForProgram')
    # os.mkdir(new_dir)
    # os.chdir(new_dir)

    os.system(f'git clone {git_teacher}')
    os.system(f'git clone {git_student}')

    new_dir_student = git_student[git_student.rfind('/') + 1:git_student.rfind('.git')]
    new_dir_teacher = git_teacher[git_teacher.rfind('/') + 1:git_teacher.rfind('.git')]
    source = os.path.join(new_dir, new_dir_student)
    dest = os.path.join(new_dir, new_dir_teacher)
    os.chdir(source)
    files = os.listdir(source)
    for f in files:
        if '.git' in f or f == 'README.md':
            continue
        shutil.move(os.path.join(source, f), dest)

    os.chdir('..')
    os.chdir(dest)
    process_finished_with_exit_code = os.system('python -m unittest main_test.TestCalc.test_calc')
    return process_finished_with_exit_code
