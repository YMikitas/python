# ЗАПИСЬ ДАННЫХ
# colors = ['red', 'green', 'blue']
# data = open('file.txt', 'a')        # а - открытие файла для добавления данных
# data.writelines(colors)             # Разделители не предусмотрены
# data.close()                        # Закрытие файла во избежание утечек памяти

# exit()                              # Прерывает выполнение кода. Код ниже не выполняется

# with open('file.txt', 'w') as data:
#     data.write('Line 1\n')
#     data.write('Line 2\n')
# В этом случае нет необходимости закрывать файл

# ЧТЕНИЕ ДАННЫХ
# path = 'file.txt'                   # Создание пути к папке
# data = open(path, 'r')              # Открытие в режиме чтения
# for line in data:                   # Цикл-проходчик
#     print(line)                     # Оператор print добавляет лишний перенос строки
# data.close()



# import Hello as h
# print(h.f(1))

# def concatenatio(*params):
#     res = 0
#     for item in params:
#         res += item
#     return res

# print(concatenatio(1, 2, 3, 4))

# КОРТЕЖ - это неизменяемый список
a = (3, 4, 5, 6 )
# print(a)
# print(a[2])
# print(a[-1])

# for item in a:
#     print(item)


# СЛОВАРЬ - это неупорядоченные коллекции произвольных объектов с доступом по ключу
dictionary = {}                     # \ возволяет разбить одну строку кода на несколько
dictionary = \
    {
        'up': 'Вверх',
        'left': 'Влево',
        'down': 'Вниз',
        'right': 'Вправо'
    }

# print (dictionary)                  # {'up': 'Вверх', 'left': 'Влево', 'down': 'Вниз', 'right': 'Вправо'}
# print(dictionary['left'])           # Влево

# for k in dictionary.keys():
#     print(k)
# for k in dictionary.values():
#     print(k)
# for v in dictionary:
#     print(v)


# МНОЖЕСТВО - неупорядоченная совокупность элементов
# colors = {'red', 'green', 'blue'}

# print(colors)                       # {'green', 'red', 'blue'}

# colors.add('red')
# print(colors)                       # {'green', 'red', 'blue'} элемент уже есть, ничего не изменилось

# colors.add('gray')
# print(colors)                       # {'green', 'gray', 'blue', 'red'}

# colors.remove('red')
# print(colors)                       # {'green', 'gray', 'blue'} 

# ## colors.remove('red')             # Попытка удаления несущестующего элемента через .remove приводит к ошибке
# ## print(colors)                    # KeyError: 'red'

# colors.discard('red')               # Удаление несуществующего элемента через .discard не вызовет ошибку
# print(colors)                       # {'gray', 'blue', 'green'}

# colors.clear()                      # Очистка множества
# print(colors)                       # set()


# a = {1, 2, 3, 5, 8}
# b = {2, 5, 8, 13, 21}
# c = a.copy()                        # c = {1, 2, 3, 5, 8}
# u = a. union(b)                     # u = {1, 2, 3, 5, 8, 13, 21}
# i = a.intersection(b)               # i = {8, 2, 5}
# dl = a.difference(b)                # dl = {1, 3}
# dr = b.difference(a)                # dr = {13, 21}

# s = frozenset(a)                    # Заморозка множества, после чего никакие добавления и удаления работать не будут


# СПИСКИ
list1 = [1, 2, 3, 4, 5]
list1.pop(2)                        # .pop удаляет элемент по индексу
print(list1)                        # [1, 2, 4, 5]

list2 = [1, 2, 3, 4, 5]
list2.insert(2, 11)                 # .insert(индекс, значение) вставляет значение на место индекса
print(list2)                        # [1, 2, 11, 3, 4, 5]

list3 = [1, 2, 3, 4, 5]
list3.append(11)                    # .append(элемент) добавляет элемент в конец списка
print(list3)                        # [1, 2, 3, 4, 5, 11]