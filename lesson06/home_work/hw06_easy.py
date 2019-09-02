# Задача-1: Написать класс для фигуры-треугольника, заданного координатами трех точек.
# Определить методы, позволяющие вычислить: площадь, высоту и периметр фигуры.
import math

class Triangle():

    def __init__(self, coord_a, coord_b, coord_c):

        self.coord_a = coord_a
        self.coord_b = coord_b
        self.coord_c = coord_c

        self.side_a = math.sqrt((coord_b[0] - coord_a[0]) ** 2 + (coord_b[1] - coord_a[1]) ** 2)
        self.side_b = math.sqrt((coord_c[0] - coord_b[0]) ** 2 + (coord_c[1] - coord_b[1]) ** 2)
        self.side_c = math.sqrt((coord_a[0] - coord_c[0]) ** 2 + (coord_a[1] - coord_c[1]) ** 2)
        self.half_p = (self.side_a + self.side_b + self.side_c) / 2


    def square(self):
        return (self.height() * self.side_a / 2)
    def height(self):
        return (2 * math.sqrt(self.half_p * ((self.half_p - self.side_a) * (self.half_p - self.side_b) * (self.half_p - self.side_c))) / self.side_a)
    def perimeter(self):
        return (self.side_a + self.side_b + self.side_c)

coord_tri_a = (1, 2)
coord_tri_b = (-1, 1)
coord_tri_c = (2, 2)

triang = Triangle(coord_tri_a, coord_tri_b, coord_tri_c)

# print(triang.side_a, triang.side_b, triang.side_c)
# print(triang.square())
# print(triang.height())
# print(triang.perimeter())



# Задача-2: Написать Класс "Равнобочная трапеция", заданной координатами 4-х точек.
# Предусмотреть в классе методы:
# проверка, является ли фигура равнобочной трапецией;
# вычисления: длины сторон, периметр, площадь.

class Trapeze():

    def __init__(self, coord_a, coord_b, coord_c, coord_d):
        self.coord_a = coord_a
        self.coord_b = coord_b
        self.coord_c = coord_c
        self.coord_d = coord_d

        self.side_a = math.sqrt((coord_b[0] - coord_a[0]) ** 2 + (coord_b[1] - coord_a[1]) ** 2)
        self.side_b = math.sqrt((coord_c[0] - coord_b[0]) ** 2 + (coord_c[1] - coord_b[1]) ** 2)
        self.side_c = math.sqrt((coord_d[0] - coord_c[0]) ** 2 + (coord_d[1] - coord_c[1]) ** 2)
        self.side_d = math.sqrt((coord_a[0] - coord_d[0]) ** 2 + (coord_a[1] - coord_d[1]) ** 2)

    @property
    def perimeter(self):
        return (self.side_a + self.side_b + self.side_c + self.side_d)

    @property
    def square(self):
        return (self.side_b + self.side_d / 4 * math.sqrt(4 * self.side_b - (self.side_b - self.side_d) ** 2))

    @property
    def isosceles(self):
        return True if self.side_a == self.side_c else False

'''
        A     d          D
        .________________.
       /                  \
     a/                    \c
     /                      \
    .________________________.
   B         b                C
'''



coord_trap_a = (-1, 1)
coord_trap_b = (-2, -1)
coord_trap_c = (2, -1)
coord_trap_d = (1, 1)

trap = Trapeze(coord_trap_a, coord_trap_b, coord_trap_c, coord_trap_d)

print(trap.isosceles)
print(trap.square)
print(trap.perimeter)
