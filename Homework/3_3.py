# 3. Напишите программу, которая будет преобразовывать десятичное число в двоичное.
#    Без использования встроенной функции преобразования, без строк.

def converter(number):
    res = []
    while number // 2 > 0:
        res.insert(0, number % 2)
        number = number // 2
        if number == 1:
            res.insert(0, 1)
        elif number == 0:
            res.insert(0, 0)

    res_finish = "".join(list(map(str, res)))
    return int(res_finish)

print(converter(int(input('Введите число для конвертации: '))))