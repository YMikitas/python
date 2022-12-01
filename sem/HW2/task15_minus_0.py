# 3 - Дан массив размера N. После каждого отрицательного элемента массива вставьте элемент с нулевым значением.

# Пример:
# - пусть N = 4, тогда [28, -46, 14, -14] => [28, -46, 0, 14, -14, 0]

import random

size = int(input('Введите размер массива: '))

list = []

for i in range(size):
    list.append(random.randint(-100, 100))
print(list)

for j, item in enumerate(list):
    if item < 0:
        list.insert(j + 1, 0)
print(list)