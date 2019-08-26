# Все задачи текущего блока решите с помощью генераторов списков!

# Задание-1:
# Дан список, заполненный произвольными целыми числами. 
# Получить новый список, элементы которого будут
# квадратами элементов исходного списка
# [1, 2, 4, 0] --> [1, 4, 16, 0]

list_a = [1, 2, 4, 0]
list_b = [itm**2 for itm in list_a]
print(list_b)

# Задание-2:
# Даны два списка фруктов.
# Получить список фруктов, присутствующих в обоих исходных списках.

fruit_list_a = ["яблоко", "банан", "киви", "арбуз", "груша"]

fruit_list_b = ["киви", "арбуз", "груша", "персик", "слива"]

fruit_list_c = []

itm = None

fruit_list_c = list(filter(lambda item: item, [itm if itm in fruit_list_b else None for itm in fruit_list_a]))
print (fruit_list_c)

# Задание-3:
# Дан список, заполненный произвольными числами.
# Получить список из элементов исходного, удовлетворяющих следующим условиям:
# + Элемент кратен 3
# + Элемент положительный
# + Элемент не кратен 4

fruit_list_d = [-135, 52, 43, 894, 105, 56, -799, 88, 459, 58, 66, 78]
fruit_list_d = list(filter(lambda item: item, [itm if itm % 3 == 0 else None for itm in fruit_list_d]))

print(fruit_list_d)

fruit_list_d = [-135, 52, 43, 894, 105, 56, -799, 88, 459, 58, 66, 78]
fruit_list_d = list(filter(lambda item: item, [itm if itm > 0 else None for itm in fruit_list_d]))

print(fruit_list_d)

fruit_list_d = [-135, 52, 43, 894, 105, 56, -799, 88, 459, 58, 66, 78, 8]
fruit_list_d = list(filter(lambda item: item, [itm if itm % 4 != 0 else None for itm in fruit_list_d]))

print(fruit_list_d)