# Дан список чисел. Создайте список, в который попадают числа,
# описывающие возрастающую последовательность.
# Порядок элементов менять нельзя.
from random import sample


def new_list_number(number: int):
    if number < 1:
        return 'Error'
    list_elements = sample(range(0, number * 2), number)
    return list_elements


def array_list(list_number: list):
    list_total = []
    for i in range(len(list_number)):
        value = list_number[i]
        list_help = [value]
        value = list_number[i]
        for j in range((i + 1), (len(list_number))):
            if list_number[j] > value:
                value = list_number[j]
                list_help.append(value)
        if len(list_help) > 1:
            list_total.append(list_help)
    return list_total


list_original = new_list_number(int(input('Enter a number: ')))
print(list_original)
print(array_list(list_original))
