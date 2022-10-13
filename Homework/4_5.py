# 5. ** Даны два файла, в каждом из которых находится запись многочленов.
# Задача - сформировать файл, содержащий сумму многочленов.

str_line = ''

file_1 = open('poly.txt', 'r')
file_2 = open('poly_2.txt', 'r')

while True:
    line1 = file_1.readline()
    line2 = file_2.readline()
    if not line2 or not line1:
        break

    str_line = line1[:-4] + '+ ' + line2
    with open('poly_all.txt', 'a', encoding='utf-8') as file_my:
        file_my.write(f'{str_line}\n')

# from random import choice
#
#
# def poly_sum(name_1: str, name_2: str):
#     with open(name_1, "r", encoding="utf-8") as my_f_1, \
#             open(name_2, "r", encoding="utf-8") as my_f_2:
#         first = my_f_1.readlines()
#         second = my_f_2.readlines()
#
#         if len(first) == len(second):
#             with open("sum_poly.txt", "a", encoding="utf-8") as my_f_3:
#                 for i, v in enumerate(first):
#                     my_f_3.write(f"{v[:-5]} + {second[i]}")
#         else:
#             print("The contents of the files do not match!")
#
#
# poly_sum(input("Enter the file name 'text_1.txt': "), input("Enter the file name 'text_2.txt': "))
# poly_sum("poly.txt", "poly_2.txt")