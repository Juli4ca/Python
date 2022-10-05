# 2. Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.

def natural_number(n):
    if n < 0:
        n = - n
    d = 2
    while n % d != 0:
        d += 1
    return d == n


def prime_factors_number(n):
    list_n = []
    while True:
        if n % 10 == 5:
            n = n // 5
            list_n.append(5)
            if natural_number(n):
                list_n.append(n)
                break
        elif n % 3 == 0:
            n = n // 3
            list_n.append(3)
            if natural_number(n):
                list_n.append(n)
                break
        elif n % 2 == 0:
            n = n // 2
            list_n.append(2)
            if natural_number(n):
                list_n.append(n)
                break

    return list_n


num = int(input("Задайте натуральное число N: "))
if -2 < num < 2:
    print("Недопустимое значение")
elif natural_number(num):
    print("Число простое")
else:
    print(prime_factors_number(num))