# Задание-1:
# Напишите функцию, возвращающую ряд Фибоначчи с n-элемента до m-элемента.
# Первыми элементами ряда считать цифры 1 1

def fibonacci(n, m):
    if n == 2:
        result = [1]
    elif n == 1:
        result = [1,1]
    else:
        result = []

    temp = [1,1]

    if n < m and m > 3:
        for idx in range(3, m):
            if idx >= n:
                result.append(temp[-2] + temp[-1])
            temp.append(temp[-2] + temp[-1])

    return result


#print(fibonacci(3, 5))


# Задача-2:
# Напишите функцию, сортирующую принимаемый список по возрастанию.
# Для сортировки используйте любой алгоритм (например пузырьковый).
# Для решения данной задачи нельзя использовать встроенную функцию и метод sort()


def sort_to_max(origin_list):
    result = origin_list
    num_len = len(origin_list)

    for idx in range(1, num_len):
        for i in range(num_len - idx):
            if result[i] > result[i + 1]:
                result[i], result[i + 1] = result[i + 1], result[i]
    return result

#print(sort_to_max([2, 10, -12, 2.5, 20, -11, 4, 4, 0, -2500]))

# Задача-3:
# Напишите собственную реализацию стандартной функции filter.
# Разумеется, внутри нельзя использовать саму функцию filter.
def new_filter(filter_func, iter):
    result = []
    for i, idx in enumerate(iter):
        if filter_func(idx):
            result.append(iter[i])
    return result

print(list(filter(lambda x: x > 5, [2, 10, -10, 8, 2, 0, 14])))
print(list(new_filter(lambda x: x > 5, [2, 10, -10, 8, 2, 0, 14])))

# Задача-4:
# Даны четыре точки А1(х1, у1), А2(x2 ,у2), А3(x3 , у3), А4(х4, у4).
# Определить, будут ли они вершинами параллелограмма.

