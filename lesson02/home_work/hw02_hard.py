# Задание-3: "Перевёрнутая башня" (Задача олимпиадного уровня)
#
# Вавилонцы решили построить удивительную башню —
# расширяющуюся к верху и содержащую бесконечное число этажей и комнат.
# Она устроена следующим образом — на первом этаже одна комната,
# затем идет два этажа, на каждом из которых по две комнаты, 
# затем идёт три этажа, на каждом из которых по три комнаты и так далее:
#         ...
#
#   27  28  29  30
#   23  24  25  26
#   19  20  21  22
#   15  16  17  18
#     12  13  14
#     9   10  11
#     6   7   8
#       4   5
#       2   3
#         1
#
# Эту башню решили оборудовать лифтом --- и вот задача:
# нужно научиться по номеру комнаты определять,
# на каком этаже она находится и какая она по счету слева на этом этаже.
#
# Входные данные: В первой строчке задан номер комнаты N, 1 ≤ N ≤ 2 000 000 000.
#
# Выходные данные:  Два целых числа — номер этажа и порядковый номер слева на этаже.
#
# Пример:
# Вход: 13
# Выход: 6 2
#
# Вход: 11
# Выход: 5 3

from math import sqrt

def tower_elevator(seecing_room):
    start_room = 0
    floors = 0

    for floore_group in range(1,2000000):
        rooms_count = start_room + floore_group ** 2
        if seecing_room in range(start_room, rooms_count + 1):

            if int((seecing_room - start_room) % sqrt(rooms_count - start_room)):
                current_group_flor = int((seecing_room - start_room) // sqrt(rooms_count - start_room)) + 1
            else:
                current_group_flor = int((seecing_room - start_room) // sqrt(rooms_count - start_room))

            if int((seecing_room - start_room) % sqrt(rooms_count - start_room)):
                room = int((seecing_room - start_room) % sqrt(rooms_count - start_room))
            else:
                room = int(sqrt(rooms_count - start_room))

            print(current_group_flor + floors , room)

            break

        start_room = start_room + floore_group ** 2
        floors += floore_group


tower_elevator(25)
