# value = None
# a = 123
# b = 1.23
# print(a)
# #print(type(a))
# print(b)
# #print(type(b))
# value = 12334
# print(value)

# s = 'hello world'
# print(s) # Вывод строки

# print(a, b, s)
# print(a, '-', b, '-', s)
# print('{1} - {2} - {0}' .format(a, b, s)) # Форматированный вывод
# print(f'{a} - {b} - {s}') # Интерполяция

# f = True
# print(f)

# list = [1, 2, 3, 'hello', True]
# print(list)

# print('input a')
# a = int(input())
# print('input b')
# b = int(input())
# print(a, ' + ', b, ' = ', a + b)

# a = 1.31278
# b = 3
# c = round(a * b, 5)
# print(c)

# a = 3
# a += 5 # a = a + 5
# print(a)

# a = int(input('a = '))
# b = int(input('b = '))
# if a > b:
#     print(a)
# else:
#     print(b)

# username = input('Введите имя: ')
# if username == 'Маша':
#     print('Ура, это же Маша!')
# elif username == "Марина":
#     print('Я так ждал вас, Марина!')
# else:
#     print('Привет, ', username)

# original = 23
# inverted = 0
# while original != 0:
#     inverted = inverted * 10 + (original % 10)
#     original //= 10
# print(inverted)

# list = [1,2,3,4,5]
# for i in list:
#     print(i ** 2)

# for i in range(1, 10, 2):
#     print(i)

def f(x):
    if x == 1:
        return 'Целое'
    elif x == 2.3:
        return 23
    else:
        return