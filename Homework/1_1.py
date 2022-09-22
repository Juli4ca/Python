# Напишите программу,
# которая принимает на вход цифру, обозначающую день недели,
# и проверяет, является ли этот день выходным.

day_of_week_num = int(input('Enter the number of the day of the week: '))
if day_of_week_num < 1 or day_of_week_num > 7:
    print('Input error')
elif day_of_week_num < 6:
    print('Weekday')
else:
    print('Weekend')