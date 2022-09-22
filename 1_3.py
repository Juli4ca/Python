# 3. Напишите программу, которая будет на вход принимать число N и выводить числа от -N

n = int(input('Input number: '))
if n < 0:
    n *= -1

for i in range(-n, n+1):
    print(i, end=' ')

num = int(input())
neg_num = -num

while num != neg_num:
    print(neg_num, end=", ")
    if num > 0:
        neg_num += 1
    else:
        neg_num -= 1
