# 1. Представлен список чисел. Необходимо вывести элементы исходного списка,
# значения которых больше предыдущего элемента. Use comprehension.
# in
# 9
#
# out
# [15, 16, 2, 3, 1, 7, 5, 4, 10]
# [16, 3, 7, 10]
from random import sample

def list_int(count: int):
    if count < 1:
        return 'Error'
    list_elements = sample(range(1, count * 3), count)
    return list_elements

def same_list(list_number: list):
    list_n = [list_number[i] for i in range(1, len(list_number)) if list_number[i] > list_number[i - 1]]
    return list_n

list_original = list_int(int(input('Enter a number: ')))
print(list_original)
print(same_list(list_original))