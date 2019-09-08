#!/usr/bin/python3

"""
== Лото ==

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
 7 11     - 14    87      
      16 49    55 77    88    
   15 20     -       76  -
--------------------------
Зачеркнуть цифру? (y/n)

Подсказка: каждый следующий случайный бочонок из мешка удобно получать 
с помощью функции-генератора.

Подсказка: для работы с псевдослучайными числами удобно использовать 
модуль random: http://docs.python.org/3/library/random.html

"""
__author__ = 'Субботин Андрей Владимирович'

import random


class LotoCard(object):

    def __init__(self):

        self.numbers = set()
        self.card_numbers = []
        self.__shufl()

    def __shufl(self):

        while len(self.numbers) < 15:

            self.numbers.add(random.randint(1,91))

        self.card_numbers = list(self.numbers)
        self.card_numbers.extend(('__',) * 12)
        random.shuffle(self.card_numbers)



class Player(object):

    def __init__(self, name = None):
        
        self.is_human = bool()
        self.name = name
        if self.name == None:
            self.name = "Компьютер"
            self.is_human = False

        else:
            self.is_human = True

    def ask(self):

        while True:
            ask = input('Зачеркнуть? y/n \n')

            if ask.lower() == 'y':
                return True
            elif ask.lower() == 'n':
                return False
            else:
                print('вы не ответили')
                continue


class Bag(object):

    def __init__(self):

        self.numbers = list(range(1, 91))
        random.shuffle(self.numbers)

    def push_barel(self):

        return self.numbers.pop()


class Lobby(object):
    def __init__(self):
        self.__bag = Bag()
        self.card1 = LotoCard()
        self.card2 = LotoCard()
        self.pleer1 = Player(input('Введите ваше имя:\n'))
        self.pleer2 = Player()

    def show_cards(self):

        print('{:-^26}'.format(f"Карточка {self.pleer1.name}"))
        print(*self.card1.card_numbers[:9])
        print(*self.card1.card_numbers[9:18])
        print(*self.card1.card_numbers[18:])
        print('--------------------------\n')
        print('{:-^26}'.format(f"Карточка {self.pleer2.name}"))
        print(*self.card2.card_numbers[:9])
        print(*self.card2.card_numbers[9:18])
        print(*self.card2.card_numbers[18:])
        print('--------------------------')

    def show_barel(self):
        return self.__bag.push_barel()
    @property
    def barel_remained(self):
        return len(self.__bag.numbers)

    @staticmethod
    def pleer_check(is_human, barel, numbers, card_numbers):

        if is_human == True:

            if barel in numbers:
                right_answer = True
            else:
                right_answer = False

            pleer_answer = lobby.pleer1.ask()

            if pleer_answer != right_answer:
                print('Вы проиграли.')
                exit(0)
            else:
                if right_answer == True:

                    card_numbers[card_numbers.index(barel)] = '--'
                    numbers.pop()

                else:
                    pass
        else:
            if barel in numbers:
                card_numbers[card_numbers.index(barel)] = '--'
                numbers.pop()

if __name__ == '__main__':
    lobby = Lobby()

    while lobby.card1.numbers and lobby.card2.numbers:

        barel = lobby.show_barel()

        print(f'Новый бочонок: {barel} (осталось {lobby.barel_remained})')
        lobby.show_cards()

        lobby.pleer_check(lobby.pleer1.is_human, barel, lobby.card1.numbers, lobby.card1.card_numbers)
        lobby.pleer_check(lobby.pleer2.is_human, barel, lobby.card2.numbers, lobby.card2.card_numbers)

    if not lobby.card1.numbers and lobby.pleer1.is_human:
        print('Вы выиграли')
    elif not lobby.card2.numbers and lobby.pleer2.is_human:
        print('Вы выиграли')
    else:
        print('Вы выиграли')