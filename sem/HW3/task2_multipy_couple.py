# 2-Напишите программу, которая найдёт произведение пар чисел списка. 
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.

# [2, 3, 4, 5, 6] => [12, 15, 16];
# [2, 3, 5, 6] => [12, 15]


def mult_list(list):
    X = len(list) // 2 + 1 if len(list) % 2 != 0 else len(list) // 2
    new_list = [list[i] * list[len(list) -i -1] for i in range(X)]
    print(new_list)

list = [4, 8, 15, 16, 23, 42, 1]
mult_list(list)