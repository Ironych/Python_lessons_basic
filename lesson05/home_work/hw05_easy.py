import os
import sys
import shutil


# Задача-1:
# Напишите скрипт, создающий директории dir_1 - dir_9 в папке, из которой запущен данный скрипт.
# И второй скрипт, удаляющий эти папки.

# for i in range(9):
#     dir_path = os.path.join(os.getcwd(), f'dir_{i+1}')
#     try:
#         os.mkdir(dir_path)
#     except FileExistsError:
#         print('Такая директория уже существует')

# for i in range(9):
#     dir_path = os.path.join(os.getcwd(), f'dir_{i+1}')
#     try:
#         os.rmdir(dir_path)
#     except FileNotFoundError:
#         print('Такой директории нет')


def mk_dir(dir_name):
    dir_path = os.path.join(os.getcwd(), dir_name)
    try:
        os.mkdir(dir_path)

    except FileExistsError:
        print('Такая директория уже существует')
    else:
        print(f'Директория {dir_path} создана')


def rm_dir(dir_name):
    dir_path = os.path.join(os.getcwd(), dir_name)
    try:
        os.rmdir(dir_path)

    except FileNotFoundError:
        print('Такой директории нет')
    else:
        print(f'Директория {dir_path} удалена')


def ch_dir(dir_name):
    dir_path = os.path.join(os.getcwd(), dir_name)
    try:
        os.chdir(dir_path)
    except FileNotFoundError:
        print('Такой директории нет')
    else:
        print(f'Выбрана директория {dir_path}')


# Задача-2:
# Напишите скрипт, отображающий папки текущей директории.

def show_dirs():
    files = os.listdir(path=os.getcwd())
    if not files:
        print('Директория пуста')
    else:
        for itm in files:
            if os.path.isdir(itm):
                print(itm)


def show_files():
    files = os.listdir(path=os.getcwd())
    if not files:
        print('Директория пуста')
    else:
        for itm in files:
            if os.path.isfile(itm):
                print(itm)


def show_all():
    files = os.listdir(path=os.getcwd())
    if not files:
        print('Директория пуста')
    else:
        for itm in files:
            print(itm)


# Задача-3:
# Напишите скрипт, создающий копию файла, из которого запущен данный скрипт.
def cp_file():
    name = os.path.basename(__file__)
    copy_filename = f'copy_of_{name}'
    copy_path = os.path.join(os.getcwd(), copy_filename)
    shutil.copyfile(sys.argv[0], copy_path)


if __name__ == "__main__":
    pass
