# 5. ** Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.

def fibonachi(num):
    if num < 1:
        return 'Некорректный ввод'
    fibonachi_list = [0, 1]

    for i in range(1, num):
        fibonachi_list.append(fibonachi_list[i] + fibonachi_list[i - 1])

    negofibonachi_list = fibonachi_list[::-1]

    for i in range(0, num - 1, 2):
        negofibonachi_list[i] = -negofibonachi_list[i]

    fibonachi_list.pop(0)
    negofibonachi_list.extend(fibonachi_list)
    return negofibonachi_list

print(fibonachi(int(input('Введите размер списка: '))))


