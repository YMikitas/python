# 5- Напишите программу, которая принимает на вход координаты двух точек и находит расстояние между ними в 2D пространстве.

# Пример:

# - A (3,6); B (2,1) -> 5.09
# - A (7,-5); B (1,-1) -> 7.21

import math

X1 = float(input('Введите X координату точки A: '))
Y1 = float(input('Введите Y координату точки A: '))
X2 = float(input('Введите X координату точки B: '))
Y2 = float(input('Введите Y координату точки B: '))

D = math.pow((X1-X2), 2) + math.pow((Y1-Y2), 2)
Distance = round(math.sqrt(D),2)
print (str(Distance))