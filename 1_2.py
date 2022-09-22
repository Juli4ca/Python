# 2. Напишите программу, которая на вход принимает 5 чисел и находит максимальное из них.

max_num = 0
for i in range(5):
    number = int(input('Input number: '))
    if number > max_num:
        max_num = number
print(max_num)