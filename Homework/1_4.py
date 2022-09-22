# Напишите программу, которая по заданному номеру четверти,
# показывает диапазон возможных координат точек в этой четверти (x и y).

querter_number = int(input('Set the quarter number: '))

if querter_number == 1:
    print('x > 0, y > 0')
elif querter_number == 2:
    print('x < 0, y > 0')
elif querter_number == 3:
    print('x < 0, y < 0')
elif querter_number == 4:
    print('x > 0, y < 0')
else:
    print('Error')