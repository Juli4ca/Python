# Напишите программу, которая принимает на вход число N и выдает последовательность и N членов.

n = int(input('Enter a number N: '))

for i in range(n):
    print((-3) ** i, end=' ')

print()
n = int(input('Enter a number N: '))
var = 1

for i in range(n):
    print(var, end=' ')
    var *= -3
