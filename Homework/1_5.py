# Напишите программу, которая принимает на вход координаты двух точек и
# находит расстояние между ними в 2D пространстве.
# *Пример:*
#
# - A (3,6); B (2,1) -> 5,09
# - A (7,-5); B (1,-1) -> 7,21

x1, y1 = int(input('Enter the coordinates of the point X1: ')), int(input('Enter the coordinates of the point Y1: '))
x2, y2 = int(input('Enter the coordinates of the point X2: ')), int(input('Enter the coordinates of the point Y2: '))
dis_points = ((x1 - x2)**2 + (y1 - y2)**2)**0.5

print(f'A ({x1}, {y1}); B ({x2}, {y2} -> {round(dis_points, 3)}')
