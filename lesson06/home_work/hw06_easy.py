# Задача-1: Написать класс для фигуры-треугольника, заданного координатами трех точек.
# Определить методы, позволяющие вычислить: площадь, высоту и периметр фигуры.
import math


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


class Vektor(Point):
    def __init__(self, x1, y1, x2, y2):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2
        self.a = Point(x1, y1)
        self.b = Point(x2, y2)

    @property
    def len(self):
        return math.sqrt((self.x2 - self.x1) ** 2 + (self.y2 - self.y1) ** 2)


class Trianle(Vektor):
    def __init__(self, x1, y1, x2, y2, x3, y3):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2
        self.x3 = x3
        self.y3 = y3
        self.a = Point(x1, y1)
        self.b = Point(x2, y2)
        self.c = Point(x3, y3)
        self.ab = Vektor(self.a.x, self.a.y, self.b.x, self.b.y)
        self.bc = Vektor(self.b.x, self.b.y, self.c.x, self.c.y)
        self.ca = Vektor(self.c.x, self.c.y, self.a.x, self.a.y)

    # Периметр
    @property
    def len_abc(self):
        return self.ab.len + self.bc.len + self.ca.len
    # Площадь
    @property
    def s_abc(self):
        return abs(((self.x2 - self.x1) * (self.y3 - self.y1) - (self.x3 - self.x1) * (self.y2 - self.y1)) )/ 2

    #высота
    @property
    def h_a(self):
        return abs(((self.x2 - self.x1) * (self.y3 - self.y1) - (self.x3 - self.x1) * (self.y2 - self.y1)) / self.bc.len)

abc = Trianle(0, 0, 0, 1, 1, 0)
print(abc)
print(abc.len_abc)
print(abc.s_abc)
print(abc.h_a)


# Задача-2: Написать Класс "Равнобочная трапеция", заданной координатами 4-х точек.
#  Предусмотреть в классе методы: проверка, является ли фигура равнобочной трапецией;
#  вычисления: длины сторон, периметр, площадь.

class Trap(Vektor):
    def __init__(self, x1, y1, x2, y2, x3, y3, x4, y4):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2
        self.x3 = x3
        self.y3 = y3
        self.x4 = x4
        self.y4 = y4
        self.a = Point(x1, y1)
        self.b = Point(x2, y2)
        self.c = Point(x3, y3)
        self.d = Point(x4, y4)
        self.ab = Vektor(self.a.x, self.a.y, self.b.x, self.b.y)
        self.bc = Vektor(self.b.x, self.b.y, self.c.x, self.c.y)
        self.cd = Vektor(self.c.x, self.c.y, self.d.x, self.d.y)
        self.da = Vektor(self.d.x, self.d.y, self.a.x, self.a.y)

    # Длины строн
    @property
    def len_ab(self):
        return self.ab.len

    # Периметр
    def len_abcd(self):
        c = self.ab.len
        d = self.cd.len
        a = self.bc.len
        b = self.da.len
        return a + b + c + d

    # Площадь
    def s_abcd(self):
        c = self.ab.len
        d = self.cd.len
        a = self.bc.len
        b = self.da.len
        if b == a:
            return a * b
        else:
            return ((a + b) / 2) * (math.sqrt((c ** 2) - ((((b - a) ** 2) + (c ** 2) - (d ** 2)) / (2 * (b - a)))))

    # проверка что ранобедренный
    def proverka(self):
        #c = math.sqrt(((self.x2 - self.x1) ** 2) + ((self.y2 - self.y1) ** 2))
        #d = math.sqrt(((self.x4 - self.x3) ** 2) + ((self.y4 - self.y3) ** 2))
        c = self.ab.len
        d = self.cd.len
        if c == d:
            print("Трапеция равнобокая")
        else:
            print("Трапеция неравнобокая")

abcd = Trap(0, 0, 0, 1, 1, 1, 0, 1)
abcd.proverka()
print(abcd.len_abcd())
print(abcd.s_abcd())
