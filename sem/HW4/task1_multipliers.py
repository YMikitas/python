# 1 - Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.
# N = 20 -> [2, 5]
# N = 30 -> [2, 3, 5]

N = abs(int(input('Введите натуральное число: ')))
multipliers_list = []


def multipliers(num: int) -> list:
    """
    Функция для нахождения всех множителей
    Args:
        num (int): Заданное число
    Returns:
       result_list: Список всех множителей
    """
    result_list = []

    d = 2
    while d * d <= num:
        if num % d == 0:
            result_list.append(d)
            num //= d
        else:
            d += 1
    if num > 1:
        result_list.append(num)
    return result_list


multipliers_list = list(multipliers(N))
print(multipliers_list)
