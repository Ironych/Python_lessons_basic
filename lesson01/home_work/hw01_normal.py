import math
__author__ = 'Сафин Алексей'

# 24.06.2019
# Задача-1: Дано произвольное целое число, вывести самую большую цифру этого числа.
# Например, дается x = 58375.
# Нужно вывести максимальную цифру в данном числе, т.е. 8.
# Подразумевается, что мы не знаем это число заранее.
# Число приходит в виде целого беззнакового.
# Подсказки:
# * постарайтесь решить задачу с применением арифметики и цикла while;
# * при желании и понимании решите задачу с применением цикла for.
#
# num = int(input("Введите целое число: "))
# max_num = 0
# while num > 0:
#     ost = num % 10
#     if max_num < ost:
#         max_num = ost
#
#     num = num // 10
# max_num = str(max_num)
# print('Максимальная цифра: ' + max_num)



# Задача-2: Исходные значения двух переменных запросить у пользователя.
# Поменять значения переменных местами. Вывести новые значения на экран.
# Решите задачу, используя только две переменные.
# Подсказки:
# * постарайтесь сделать решение через действия над числами;
# * при желании и понимании воспользуйтесь синтаксисом кортежей Python.
# a = int(input("Введите число a: "))
# b = int(input("Введите число b: "))
# a = a + b
# b = a - b
# a = a - b
# print("Значение a: " + str(a) +"\nЗначение b: " + str(b))

# Задача-3: Напишите программу, вычисляющую корни квадратного уравнения вида
# ax² + bx + c = 0.
# Коэффициенты уравнения вводятся пользователем.
# Для вычисления квадратного корня воспользуйтесь функцией sqrt() модуля math:
# import math
# math.sqrt(4) - вычисляет корень числа 4


a = int(input("Введите число a: "))
b = int(input("Введите число b: "))
c = int(input("Введите число c: "))

d = b * b - 4 * a * c  # Считаем дискриминант
if d > 0:
    x1 = (-b + math.sqrt(d))/(2 * a)
    x2 = (-b - math.sqrt(d))/(2 * a)
    print ("x1 = "+ str(x1) + " x2 = "+ str(x2))
elif d == 0:
    x1 = -b /(2*a)
    print ("x1, x2 ="+ str(x1))
else:
    print("Действительных корней нет")

