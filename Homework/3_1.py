#1. Задайте список, состоящий из произвольных чисел, количество задаёт пользователь.
#   Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётных позициях(не индексах).

from random import sample

def list_int(count):
    if count < 1:
        return 'Error'
    list_elements = sample(range(1, count * 3), count)
    return list_elements

def sum_elements(new_list):
    size = len(new_list)
    sum_e = new_list[0]
    for i in range(2, size, 2):
        sum_e += new_list[i]
    return sum_e

my_list = list_int(int(input('Введите длину списка: ')))
print(my_list)
print(sum_elements(my_list))

