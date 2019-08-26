# Задание-1:
# Напишите функцию, округляющую полученное произвольное десятичное число
# до кол-ва знаков (кол-во знаков передается вторым аргументом).
# Округление должно происходить по математическим правилам (0.6 --> 1, 0.4 --> 0).
# Для решения задачи не используйте встроенные функции и функции из модуля math.

def my_round(number, ndigits):
    
    operate_num = number * 10**ndigits

    if operate_num % 1 >= 0.5:
        return (operate_num + 1) // 1 / 10**ndigits
    else:
        return operate_num // 1 / 10**ndigits
	
print(my_round(0.0045, 3))
	

print(my_round(2.1234567, 5))
print(my_round(2.1999967, 5))
print(my_round(2.9999967, 5))


# Задание-2:
# Дан шестизначный номер билета. Определить, является ли билет счастливым.
# Решение реализовать в виде функции.
# Билет считается счастливым, если сумма его первых и последних цифр равны.
# !!!P.S.: функция не должна НИЧЕГО print'ить

def lucky_ticket(ticket_number):
    if (int(str(ticket_number)[-1]) + int(str(ticket_number)[-2])) == \
       (int(str(ticket_number)[0]) + int(str(ticket_number)[1])):

        return True
    else:
        return False

print(lucky_ticket(123006))
print(lucky_ticket(12321))
print(lucky_ticket(436751))