__author__ = 'Cафин Алексей'

# Задача-1:
# Дан список фруктов. Напишите программу, выводящую фрукты в виде нумерованного списка, выровненного по правой стороне
# Пример:
# Дано: ["яблоко", "банан", "киви", "арбуз"]
# Вывод:
# 1. яблоко
# 2.  банан
# 3.   киви
# 4.  арбуз

# Подсказка: использует метод .format()

var = ["яблоко", "банан", "киви", "арбуз"]

max_len = 0

for i in var:
    if max_len < len(i):
        max_len = len(i)

for num, idx in enumerate(var):
    print(f"{num+1}.{idx:>{max_len}}")


# Задача-2:
# Даны два произвольные списка. Удалите из первого списка элементы, присутствующие во втором списке.

var1 = [44, 67, 3, 3, "яблоко", "банан", "киви", "арбуз"]
var2 = ["яблоко", "банан", 3, 9]

for x in var2:
    while var1.count(x) > 0:
        var1.remove(x)

print(var1)

# Задача-3:
# Дан произвольный список из целых чисел. Получите НОВЫЙ список из элементов исходного, выполнив следующие условия:
# если элемент кратен двум, то разделить его на 4, если не кратен, то умножить на два.

var3 = [44, 67, 3, 3, 5, 4, 6, 98, 1156, 178]
var4 = []

for x in var3:
    if x % 2 == 0:
        var4.append(x / 4)
    else:
        var4.append(x * 2)
print(var4)