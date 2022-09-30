#2. Напишите программу, которая найдёт произведение пар чисел списка.
#   Парой считаем первый и последний элемент, второй и предпоследний и т.д.

from random import sample

def list_int(count):
    if count < 1:
        return 'Error'
    list_elements = sample(range(1, count * 3), count)
    return list_elements

def product_pairs_num(new_list):
    res = 0
    length = len(new_list)
    res_list = []
    for i in range(length//2):
        res = new_list[i] * new_list[length - i - 1]
        res_list.append(res)
    if length % 2:
        res_list.append(new_list[length//2])
    return res_list

my_list = list_int(int(input('Введите длину списка: ')))
print(my_list)
if my_list != 'Error':
    print(product_pairs_num(my_list))
else:
    print('List creation error')
