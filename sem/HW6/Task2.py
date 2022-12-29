# 2- Найти произведение пар чисел в списке. Парой считаем первый и последний элемент, второй и предпоследний и т.д.

import random

mult_of_nums = []

num = int(input('Введите количество элементов массива: '))
list_of_nums = [random.randint(-10, 10) for i in range(num)]
print(list_of_nums)

mult_of_nums = [list_of_nums[i]*list_of_nums[-1 - i]

for i in range(len(list_of_nums)//2 + len(list_of_nums) % 2)]

print(mult_of_nums)