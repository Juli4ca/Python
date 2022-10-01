# 5. ** Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.

# def fibonachi(num):
#     if num < 1:
#         return 'Некорректный ввод'
#     fibonachi_list = [0, 1]
#
#     for i in range(1, num):
#         fibonachi_list.append(fibonachi_list[i] + fibonachi_list[i - 1])
#
#     negofibonachi_list = fibonachi_list[::-1]
#
#     for i in range(0, num - 1, 2):
#         negofibonachi_list[i] = -negofibonachi_list[i]
#
#     fibonachi_list.pop(0)
#     negofibonachi_list.extend(fibonachi_list)
#     return negofibonachi_list
#
# print(fibonachi(int(input('Введите число: '))))

# def fibonachi(num):
#     if num < 1:
#         return 'Enter error'
#     a, b = 1, 1
#     list_nums = [0]
#
#     for i in range(num):
#         list_nums.append(a)
#         list_nums.insert(0, a)
#         a, b = b, a + b
#
#     if num % 2:
#         for i in range(1, num - 1, 2):
#             list_nums[i] = -list_nums[i]
#     else:
#         for i in range(0, num - 1, 2):
#             list_nums[i] = -list_nums[i]
#
#     return list_nums

def fibonachi(num):
    if num < 1:
        return 'Enter error'
    a, b = 1, 1
    list_nums = [1, 0, 1]

    for i in range(1, num):
        a, b = b, a + b
        list_nums.append(a)
        list_nums.insert(0, a * (-1)**i)

    return list_nums

print(fibonachi(int(input('Enter a number: '))))




