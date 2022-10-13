# 2. Для чисел в пределах от 20 до N найти числа, кратные 20 или 21. Use comprehension.
# in
# 100
#
# out
# [20, 21, 40, 42, 60, 63, 80, 84, 100]
#
# in
# 424
#
# out
# [20, 21, 40, 42, 60, 63, 80, 84, 100, 105, 120,
# 126, 140, 147, 160, 168, 180, 189, 200, 210, 220,
# 231, 240, 252, 260, 273, 280, 294, 300, 315, 320,
# 336, 340, 357, 360, 378, 380, 399, 400, 420]

def multiples(n: int, div1: int, div2: int):
    list_number = [i for i in range(20, n + 1)]
    list_mult = [i for i in list_number if (i % div1 == 0) or (i % div2 == 0)]
    return list_mult


print(multiples(int(input('Range from 20 to: ')), int(input('Divider 1: ')), int(input('Divider 2: '))))
