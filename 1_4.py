# 4. Напишите программу, которая будет принимать на вход дробь
#    и показывать первую цифру дробной части числа.

num = float(input('Input number: '))
print(int(num * 10 % 10))