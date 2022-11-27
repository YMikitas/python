# 2. Напишите программу, в которой пользователь будет задавать две строки, а программа - определять количество вхождений одной строки в другой.

# list_1 = input('Введите строку:\n')
# list_2 = input('Введите строку:\n')
# n = 0
# for first in range(len(list_1) - len(list_2) + 1):
#     if list_1[first:first+len(list_2)] == list_2:
#         n += 1
# print(n)

a = list(input('Введите первую строку: '))
b = list(input('Введите вторую строку: '))
count = 0
for i in range(len(a) - len(b) + 1):
    if a[i] == b[0]:
        switch = True
        for j in range(len(b)):
            if a[i + j] != b[j]:
                switch = False
                break
        if switch:
            count += 1
print(count)