# Создайте список, длины n, значения формируются по формуле 3k + 1,
# где k принимает значение от 1 до n включительно.

length = int(input('Enter the length of the list: '))
s = []

for i in range(1,length + 1):
    s.append(3 * i + 1)
print(s)