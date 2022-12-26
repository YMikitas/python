# 1-Напишите программу, удаляющую из текста все слова, содержащие заданную строку.

# Пример:
# Пугать ты галок пугай => заданная строка "пугай" => Пугать ты галок

text = input('Введите исходный текст: ')

def del_word(text: str):
    for_del = input('Что требуется удалить? >>> ')
    text = list(filter(lambda x: for_del not in x, text.split()))
    return " ".join(text)


text = del_word(text)
print(text)
