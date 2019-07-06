# Задание-1:
# Напишите функцию, округляющую полученное произвольное десятичное число
# до кол-ва знаков (кол-во знаков передается вторым аргументом)
# Округление должно происходить по математическим правилам (0.6 --> 1, 0.4 --> 0).
# Для решения задачи не используйте встроенные функции и функции из модуля math


def my_round(number, ndigits):

    number = int(number*10**(ndigits+1))

    if (number%10 < 5):
        number = int(number/10)
    else:
        number = int(number/10) + 1

    result = str(number/10**ndigits)

    return result


#print(my_round(1112.12334567, 5))



# Задание-2:
# Дан шестизначный номер билета. Определить, является ли билет счастливым.
# Решение реализовать в виде функции.
# Билет считается счастливым, если сумма его первых и последних цифр равны.
# !!!P.S.: функция не должна НИЧЕГО print'ить


from functools import reduce

def sum3(items):
    sum_all = reduce(lambda x,y: x + y, items)
    return sum_all

def lucky_ticket(ticket_number):
    """
    Функция возвращает счатливый билет ли нет
    :param ticket_number:
    :return: result
    """
    ticket_number = str(ticket_number)
    result = "увы, но ваш билет не является счастливым"


    if len(ticket_number) != 6 or not ticket_number.isdigit:
        result = "Номер билета не 6-тизначным числом"
    else:
        ticket_half1 = list(ticket_number[:3])
        ticket_half2 = list(ticket_number[3:])
        ticket_half1 = list(map(int, ticket_half1))
        ticket_half2 = list(map(int, ticket_half2))
        if sum3(ticket_half1) == sum3(ticket_half2):
            result = "Поздравляю, Ваш Билет является счастливым!!!"

    return result


#print(lucky_ticket(19548.5))

