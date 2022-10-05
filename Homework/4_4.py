# 4.* Задана натуральная степень k. Сформировать случайным образом список коэффициентов
# (от 0 до 10) многочлена, записать в файл полученный многочлен не менее 3-х раз.
from random import choices, choice


def polynomial(degree):
    list_polynomial = choices(range(10), k=degree)
    for i in range(degree):
        if list_polynomial[i] > 0:
            polynom = list_polynomial[i]
            break
    sign = choice('+-')
    str_polynomial = f'{polynom}*x^{degree} {sign} '

    for i in range(degree - 1, 1, -1):
        polynom = choice(list_polynomial)
        if polynom > 0:
            sign = choice('+-')
            str_polynomial += f'{polynom}*x^{i} {sign} '
    polynom = choice(list_polynomial)
    str_polynomial += f'{polynom} = 0'
    with open('poly.txt', 'a', encoding='utf-8') as my_file:
        my_file.write(f'{str_polynomial}\n')

def polynomial_1(degree):
    list_polynomial = choices(range(10), k=degree)
    for i in range(degree):
        if list_polynomial[i] > 0:
            polynom = list_polynomial[i]
            break
    sign = choice('+-')
    str_polynomial = f'{polynom}*x^{degree} {sign} '

    for i in range(degree - 1, 1, -1):
        polynom = choice(list_polynomial)
        if polynom > 0:
            sign = choice('+-')
            str_polynomial += f'{polynom}*x^{i} {sign} '
    polynom = choice(list_polynomial)
    str_polynomial += f'{polynom} = 0'
    with open('poly_2.txt', 'a', encoding='utf-8') as my_file_1:
        my_file_1.write(f'{str_polynomial}\n')



for i in range(3):
    degree_1 = int(input("Задана натуральная степень k: "))
    if degree_1 > 2:
        polynomial(degree_1)
    else:
        print("Ошибка ввода")

for i in range(3):
    degree_2 = int(input("Задана натуральная степень k: "))
    if degree_2 > 2:
        polynomial_1(degree_2)
    else:
        print("Ошибка ввода")