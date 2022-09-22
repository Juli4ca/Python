# 5. Напишите программу, которая принимает на вход число и проверяет,
#    кратно ли оно 5 и 10 или 15, но не 30.

num = int(input('Input number: '))
if (num % 5 == 0) and num % 10 or num % 15 and num % 30:
    print('Yes')
else:
    print('No')


