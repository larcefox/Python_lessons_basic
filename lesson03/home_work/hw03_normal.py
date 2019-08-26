# Задание-1:
# Напишите функцию, возвращающую ряд Фибоначчи с n-элемента до m-элемента.
# Первыми элементами ряда считать цифры 1 1

def fibonacci(n, m):
    fibonacci = [1, 1]
	
    while m > len(fibonacci):
        fibonacci.append(fibonacci[-1] + fibonacci[-2])
		
    return fibonacci[n-1:m]

print (fibonacci(1, 30))

# Задача-2:
# Напишите функцию, сортирующую принимаемый список по возрастанию.
# Для сортировки используйте любой алгоритм (например пузырьковый).
# Для решения данной задачи нельзя использовать встроенную функцию и метод sort()


def sort_to_max(origin_list):

    sorted_list = [origin_list[0]]
	
    for origin_num in origin_list[1:]:
		
        for sorted_num in sorted_list[::-1]:
		
            if origin_num < sorted_num:
                
                if sorted_list.index(sorted_num)== 0:

                    sorted_list.insert(0, origin_num)
                    break
            
            else:

                sorted_list.insert(sorted_list.index(sorted_num) + 1, origin_num)

                break

    print(sorted_list)
			

sort_to_max([2, 10, -12, 2.5, 20, -11, 4, 4, 0])

# Задача-3:
# Напишите собственную реализацию стандартной функции filter.
# Разумеется, внутри нельзя использовать саму функцию filter.

def user_filter(func, itterible):
    filtred_args = []
    for itm in itterible:
        if func(itm):
            filtred_args.append(itm)

    return tuple(filtred_args)
	
print(list(user_filter(lambda x: x > 5, [2, 10, -10, 8, 2, 0, 14])))

# Задача-4:
# Даны четыре точки А1(х1, у1), А2(x2 ,у2), А3(x3 , у3), А4(х4, у4).
# Определить, будут ли они вершинами параллелограмма.

def parallelogram(a1, a2, a3, a4):
        for axis in zip(a1, a2, a3, a4):
            axis = sorted(axis)
            if (axis[0] - axis[1]) == (axis[2] - axis[3]):
                pass
            else:
                return False
        return True
	
	
	
a1 = (-2, 2)
a2 = (-2 ,-2)
a3 = (1, 1)
a4 = (1, -1)


print(parallelogram(a1, a2, a3, a4))