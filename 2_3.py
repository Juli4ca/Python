# Напишите программу, в которой пользователь будет задавать две строки,
# программа - определять количество вхождений одной строки в другую.

str_1 = input('Enter the first line: ')
str_2 = input('Enter the second line: ')

if str_1 in str_2:
    print(str_2.count(str_1))
elif str_2 in str_1:
    print(str_1.count(str_2))
else:
    print('0')