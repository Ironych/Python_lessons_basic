import hw05_easy

# Задача-1:
# Напишите небольшую консольную утилиту, позволяющую работать с папками текущей директории.
# Утилита должна иметь меню выбора действия, в котором будут пункты:
# 1. Перейти в папку
# 2. Просмотреть содержимое текущей папки
# 3. Удалить папку
# 4. Создать папку
# При выборе пунктов 1, 3, 4 программа запрашивает название папки
# и выводит результат действия: "Успешно создано/удалено/перешел", "Невозможно создать/удалить/перейти"

# Для решения данной задачи используйте алгоритмы из задания easy,
# оформленные в виде соответствующих функций, и импортированные в данный файл из easy.py


n = '2'
while n in ('1', '2', '3', '4'):
    print(""" 
    1. Перейти в папку
    2. Просмотреть содержимое текущей папки
    3. Удалить папку
    4. Создать папку
    5. Выход""")
    n = input('Выберете действие: \n')
    if n == '1':
        dir_name = input('Введите имя директории: \n')
        hw05_easy.ch_dir(dir_name)
    elif n == '2':
        hw05_easy.show_all()
    elif n == '3':
        dir_name = input('Введите имя директории: \n')
        hw05_easy.rm_dir(dir_name)
    elif n == '4':
        dir_name = input('Введите имя директории: \n')
        hw05_easy.mk_dir(dir_name)
    else:
        n = '5'

print('Пока')
