# Lambda (анонимные) функции

# def f(x):
#     return x**2

# g = f

# print(f(3))                     # —> 9
# print(g(4))                     # —> 16

# def calc1(x):
#     return x + 10

# print(calc(10))

# def calc2(x):
#     return x * 10

# def math(op, x):
#     print(op(x))

# math(calc2, 10)
# math(calc1, 30)

## def sum(x, y):               # то же самое sum = lambda x, y: x + y
##     return x + y

# sum = lambda x, y: x + y + 1

# def mylt(x, y):
#     return x * y

def calc(op, a, b):
    print(op(a, b))

calc(lambda x, y: x + y, 4, 6)
calc(lambda x, y: x * y, 5, 6)




## List Comprehension
## [exp for item in iterable]
## [exp for item in iterable (if conditional)]
## [exp <if conditional> for item in iterable (if conditional)]

# list = []
# for i in range(1, 21):
#     # if(i%2 == 0):
#         list.append(i)

# print (list)

# list_all = [i for i in range(1, 21)]
# print (list_all)

# list_odd = [i for i in range(1, 21) if i % 2 == 0]
# print (list_odd)


# def f(x):
#     return x**3
# list_cube = [(i, f(i)) for i in range(1, 21) if i % 2 == 0]
# print(list_cube)





# path = 'Z:/python/lec/file.txt'
# f = open(path, 'r')
# data = f.read() + ' '
# f.close()

# numbers = []                                # Создание пустого списка

# while data != '':                           # Пока строка не пустая
#     space_pos = data.index(' ')             # Найти первую позицию пробела
#     numbers.append(int(data[:space_pos]))   # Всё от первого символа до пробела превратить в число и добавить в список чисел
#     data = data[space_pos + 1]              # Обновить список

# out = []                                    # Создать новый список
# for e in numbers:                           # Пройдясь по исходному 
#     if not e in numbers:
#         if not e % 2:                       # Проверка, что число является чётным
#             out.append((e, e ** 2))         # Кортеж, где первой координатой идёт число, авторой квадрат этого числа
# print(out)


# Выбрать чётные числа и составить список пар (число, квадрат числа)
# def select(f, col):
#     return[f(x) for x in col]

# def where(f, col):
#     return[x for x in col if f(x)]
# data = '1 2 3 4 5 6 7 8 9 10'.split()
# res = select(int, data)
# res = where(lambda x: not x % 2, res)
# res = select(lambda x:(x, x ** 2), res)
# print(res)



data = '1 2 3 4 5 6 7 8 9 10'.split()
res = map(int, data)
res = filter(lambda x: not x % 2, res)
res = list(map(lambda x:(x, x ** 2), res))
print(res)


## Map
# li = [x for x in range(1, 11)]
# li = list(map(lambda x:x+10, li))
# print(li)

# data = list(map(int, input().split()))
# for e in data:
#     print(e * 10)


## Filter
# data = [x for x in range(10)]
# res = list(filter(lambda x: not x % 2, data))
# print(res)

## Zip
# users = ['U1', 'U2', 'U3', 'U4', 'U5']
# ids = [4, 5, 9, 14, 7]

# data = list(zip (users, ids))
# print(data)

## Enumerate
users = ['U1', 'U2', 'U3', 'U4', 'U5']
data = list(enumerate(users))
print(data)