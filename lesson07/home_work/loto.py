import random
import sys

# !/usr/bin/python3

"""Лото

Правила игры в лото.

Игра ведется с помощью специальных карточек, на которых отмечены числа, 
и фишек (бочонков) с цифрами.

Количество бочонков — 90 штук (с цифрами от 1 до 90).

Каждая карточка содержит 3 строки по 9 клеток. В каждой строке по 5 случайных цифр, 
расположенных по возрастанию. Все цифры в карточке уникальны. Пример карточки:

--------------------------
    9 43 62          74 90
 2    27    75 78    82
   41 56 63     76      86 
--------------------------

В игре 2 игрока: пользователь и компьютер. Каждому в начале выдается 
случайная карточка. 

Каждый ход выбирается один случайный бочонок и выводится на экран.
Также выводятся карточка игрока и карточка компьютера.

Пользователю предлагается зачеркнуть цифру на карточке или продолжить.
Если игрок выбрал "зачеркнуть":
	Если цифра есть на карточке - она зачеркивается и игра продолжается.
	Если цифры на карточке нет - игрок проигрывает и игра завершается.
Если игрок выбрал "продолжить":
	Если цифра есть на карточке - игрок проигрывает и игра завершается.
	Если цифры на карточке нет - игра продолжается.
	
Побеждает тот, кто первый закроет все числа на своей карточке.

Пример одного хода:

Новый бочонок: 70 (осталось 76)
------ Ваша карточка -----
 6  7          49    57 58
   14 26     -    78    85
23 33    38    48    71   
--------------------------
-- Карточка компьютера ---
 7 87     - 14    11      
      16 49    55 88    77    
   15 20     -       76  -
--------------------------
Зачеркнуть цифру? (y/n)

Подсказка: каждый следующий случайный бочонок из мешка удобно получать 
с помощью функции-генератора.

Подсказка: для работы с псевдослучайными числами удобно использовать 
модуль random: http://docs.python.org/3/library/random.html

"""


class Row:
    def __init__(self, start, b):
        self.i = start
        self.len = b + 1
        self.row = [i for i in range(1, self.len)]
        random.shuffle(self.row)

    def __next__(self):
        self.i += 1
        if self.i <= self.len:
            return self.i
        else:
            raise StopIteration


class Kard:
    def __init__(self, l1:list, l2:list, l3:list):
        self.l1 = sorted(list(l1))
        self.l2 = sorted(list(l2))
        self.l3 = sorted(list(l3))

    def __next__(self):
        self.i += 1
        if self.i <= self.len:
            return self.i
        else:
            raise StopIteration


    def __str__(self):
        result = f''
        for i in self.l1:
            result = result + str(i) + ' '
        result = result + '\n'
        for i in self.l2:
            result = result + str(i) + ' '
        result = result + '\n'
        for i in self.l3:
            result = result + str(i) + ' '
        result = result + '\n'
        return result

    def change(self, x):
        self.l1 = self.l1.insert(self.l1.index(x), '*')
        self.l1.pop(self.l1.index(x))
        self.l2 = self.l2.insert(self.l2.index(x), '*')
        self.l2.pop(self.l2.index(x))
        self.l3 = self.l3.insert(self.l3.index(x), '*')
        self.l3.pop(self.l3.index(x))

def player_step(x):
    ans = input('Зачеркнуть цифру? (y/n): ')
    if ans == 'y':
        if x in kard1:
            kard_p1.change(x)
            print('\nПродолжаем...')
            return 1
        else:
            print('\nИгра закончена')
            sys.exit
    if ans == 'n':
        if x in kard1:
            print('\nИгра закончена')
            sys.exit()
        else:
            print('\nПродолжаем...')


# # сгенеририм
# bag = [i for i in range(1,91)]
# # Перемешаем
# random.shuffle(bag)
# # превратим итератор
# bag_iter = iter(bag)

bag = random.sample(range(1, 91), 90)
kards = random.sample(range(1, 91), 30)

kard1 = random.sample(kards, 15)
kard2 = [x for x in kards if not x in kard1]

kard_p1 = Kard(kard1[:5], kard1[5:10], kard1[10:])
kard_p2 = Kard(kard2[:5], kard2[5:10], kard2[10:])


print('карточка игрока')
print(kard_p1)

print('карточка компа')
print(kard_p2)

for i, x in enumerate(bag):
    print(f'Новый бочонок {x}, осталось {90 - i}')
    player_step(x)
    #comp_step(x)