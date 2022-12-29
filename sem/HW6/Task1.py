# 1- Определить, позицию второго вхождения строки в списке либо сообщить, что её нет.
# Примеры
# список: ["qwe", "asd", "zxc", "qwe", "ertqwe"], ищем: "qwe", ответ: 3
# список: ["йцу", "фыв", "ячс", "цук", "йцукен", "йцу"], ищем: "йцу", ответ: 5
# список: ["йцу", "фыв", "ячс", "цук", "йцукен"], ищем: "йцу", ответ: -1
# список: ["123", "234", 123, "567"], ищем: "123", ответ: -1
# список: [], ищем: "123", ответ: -1

def input_list():
    data = input('Введите значения через пробел: ').split(" ")
    return data


def input_search():
    data = input('Что найти? >>> ')
    return data


def find_index(data_list: list[str], search_index: str) -> int:
    indexes = [i for i, string in enumerate(data_list) if search_index in string]
    try:
        return indexes[1]
    except IndexError:
        return -1


elements = input_list()
search_element = input_search()
result = find_index(elements, search_element)
print(result)