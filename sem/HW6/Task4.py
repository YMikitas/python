# 4 - Дан список случайных чисел. Оставьте только те, сумма цифр которых четна

import random

num = int(input('Введите количество элементов: '))
list_of_numbers = [random.randint(1, 100) for i in range(num)]
print(list_of_numbers)


res_sum = []
for i in list_of_numbers:
    res_sum.append(sum(map(int, str(i))))


def filt_num(num: int) -> int:
    if (num % 2) == 0:
        return True
    else:
        return False


result_list = list(filter(filt_num, res_sum))
print(result_list)