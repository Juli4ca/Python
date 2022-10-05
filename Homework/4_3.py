# 3. Задайте последовательность чисел. Напишите программу,
# которая выведет список неповторяющихся элементов исходной последовательности в том же порядке.

from random import choices


def list_int(count):
    if count < 1:
        print('Error! Negative value of the number of numbers!')
        return 0
    list_elements = choices(range(10), k=count)
    return list_elements


def list_unique(list_n):
    unique_list = []
    for i in list_n:
        if list_n.count(i) == 1:
            unique_list.append(i)
    return unique_list


my_list = list_int(int(input('List length: ')))
if my_list:
    print(my_list)
    print(list_unique(my_list))
