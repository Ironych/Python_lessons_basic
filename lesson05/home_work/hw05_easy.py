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
#     except FileExistsError:
#         print('Такой директории нет')


# Задача-2:
# Напишите скрипт, отображающий папки текущей директории.

# files = os.listdir(path=os.getcwd())
# for itm in files:
#     if os.path.isdir(itm):
#         print(itm)

# Задача-3:
# Напишите скрипт, создающий копию файла, из которого запущен данный скрипт.
name = os.path.basename(__file__)
copy_filename = f'copy_of_{name}'
copy_path = os.path.join(os.getcwd(), copy_filename)
shutil.copyfile(sys.argv[0],copy_path)