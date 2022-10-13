# 1. Вычислить число c заданной точностью d

from decimal import Decimal


def precision_num(number, number_precision):
    if number_precision < 2:
        print('Error')
    else:
        precision = '1.0' + (number_precision - 2) * '0'
        number = number.quantize(Decimal(precision))
    return number


n = Decimal(input('Enter a number: '))
n_precision = int(input('Set the precision of the number: '))
print(precision_num(n, n_precision))