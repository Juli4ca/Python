# 4.* Задайте список из произвольных вещественных чисел, количество задаёт пользователь.
# Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов.

from random import random, uniform

def list_float(count):
    if count < 1:
        return 'Error'
    list_elements = []
    for i in range(count):
        list_elements.append(round(random(), 2))
    return list_elements

def list_float_1(count):
    if count < 1:
        return 'Error'
    list_elements = []
    for i in range(count):
        list_elements.append(round(uniform(-10, 10), 2))
    return list_elements


def min_max_fraction(new_list):
    length = len(new_list)
    if new_list[0] < 0:
        new_list[0] = -new_list[0]
    min_fraction = new_list[0] % 1
    max_fraction = new_list[0] % 1
    for i in range(1, length):
        if new_list[i] < 0:
            new_list[i] = -new_list[i]
        elif min_fraction > new_list[i] % 1:
            min_fraction = new_list[i] % 1
        elif max_fraction < new_list[i] % 1:
            max_fraction = new_list[i] % 1

    res = round(max_fraction - min_fraction, 2)
    return res

list_1 = list_float(int(input('Введите размер списка: ')))
print(list_1)

print(min_max_fraction(list_1))

list_2 = list_float_1(int(input('Введите размер списка: ')))
print(list_2)

print(min_max_fraction(list_2))