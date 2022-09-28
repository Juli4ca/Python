# 1. Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.

num = float(input('Enter a real number: '))

l = len(str(num))
num = int(num * 10 ** l)
sum_num = 0

while num != 0:
    sum_num += num % 10
    num = num // 10

print(sum_num)