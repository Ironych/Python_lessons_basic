# Задание-1:
# Доработайте реализацию программы из примера examples/5_with_args.py,
# добавив реализацию следующих команд (переданных в качестве аргументов):
#   cp <file_name> - создает копию указанного файла
#   rm <file_name> - удаляет указанный файл (запросить подтверждение операции)
#   cd <full_path or relative_path> - меняет текущую директорию на указанную
#   ls - отображение полного пути текущей директории
# путь считать абсолютным (full_path) - в Linux начинается с /, в Windows с имени диска
# все остальные пути считать относительными.

# Важно! Все операции должны выполняться в той директории, в который вы находитесь. Исходной директорией считать ту,
# в которой был запущен скрипт.

# P.S. По возможности, сделайте кросс-платформенную реализацию.

import os
import sys
import shutil

print('sys.argv = ', sys.argv)


def print_help():
    print("help - получение справки")
    print("mkdir <dir_name> - создание директории")
    print("cp <file_name> - создает копию указанного файла")
    print("rm <file_name> - удаляет указанный файл (запросить подтверждение операции)")
    print("cd <full_path or relative_path> - меняет текущую директорию на указанную")
    print("ls - отображение полного пути текущей директории")
    print("ping - тестовый ключ")


def cd():
    if not dir_name:
        print("Необходимо указать имя директории вторым параметром")
        return
    if os.path.exists(dir_name):
        dir_path = dir_name
    else:
        dir_path = os.path.join(os.getcwd(), dir_name)
    try:
        os.chdir(dir_path)
    except FileNotFoundError:
        print('Такой директории нет')
    else:
        print(f'Выбрана директория {dir_path}')


def ls():
    print(os.getcwd())


def rm_file():
    if not dir_name:
        print("Необходимо указать имя файла вторым параметром")
        return
    dir_path = os.path.join(os.getcwd(), dir_name)
    suggest = ''

    if os.path.exists(dir_path):
        suggest = input('Точно удалить? (Y/N)\n')
    else:
        print('Файл {} не существует'.format(dir_name))

    if suggest.lower() == 'y':
        try:
            os.remove(dir_path)
            print('Файл {} удален'.format(dir_name))
        except FileNotFoundError:
            print('Файл {} не существует'.format(dir_name))


def cp_file():
    if not dir_name:
        print("Необходимо указать имя файла вторым параметром")
        return
    dir_path = os.path.join(os.getcwd(), dir_name)
    try:
        shutil.copy(dir_path, f'{dir_path}_copy')
        print('Копия файла {} создана'.format(dir_name))
    except FileExistsError:
        print('Копия файл {} уже существует'.format(dir_name))
    except FileNotFoundError:
        print('Файл {} не существует'.format(dir_name))


def make_dir():
    if not dir_name:
        print("Необходимо указать имя директории вторым параметром")
        return
    dir_path = os.path.join(os.getcwd(), dir_name)
    try:
        os.mkdir(dir_path)
        print('директория {} создана'.format(dir_name))
    except FileExistsError:
        print('директория {} уже существует'.format(dir_name))


def ping():
    print("pong")


do = {
    "help": print_help,
    "mkdir": make_dir,
    "cp": cp_file,
    "cd": cd,
    "rm": rm_file,
    "ls": ls,
    "ping": ping
}

try:
    dir_name = sys.argv[2]
except IndexError:
    dir_name = None

try:
    key = sys.argv[1]
except IndexError:
    key = None

if key:
    if do.get(key):
        do[key]()
    else:
        print("Задан неверный ключ")
        print("Укажите ключ help для получения справки")
