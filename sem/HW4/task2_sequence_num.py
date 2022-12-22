# 2 - Задайте последовательность чисел. 
# Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности. 
# Не использовать множества.
# Постарайтесь решить за одно условие
# [1,1,1,1,2,2,2,3,3,3,4] -> [1,2,3,4]

def get_unique_num(numbers) -> list: 
    """
    Функция для поиска неповторяющихся значений списка
    Returns:
        unique: список неповторяющихся значений списка
    """
    unique = []
    for num in numbers:
        if num in unique:
            continue
        else:
            unique.append(num)
    return unique


num_list = [1, 1, 1, 1, 2, 2, 2, 3, 3, 3, 4]
print(num_list)

print(get_unique_num(num_list))