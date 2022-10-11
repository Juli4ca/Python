# Создайте список из N натуральных чисел. Среди чисел не хватает одного,
# чтобы выполнялось условие A[i] - 1 = A[i - 1]. Найдите это число.
from random import choice


def list_num(num: int):
    list_n = [x for x in range(num - 1)]
    list_n.remove(choice(list_n))
    return list_n


def find(list_number):
    for i in range(1, len(list_number)):
        if list_number[i] - (list_number[i - 1]) > 1:
            return list_number[i] - 1
    return -1


list1 = list_num(int(input('Enter a number: ')))
print(list1)
print(find(list1))
