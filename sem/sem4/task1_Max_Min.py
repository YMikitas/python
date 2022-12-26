# 1. Задайте строку из набора чисел. Напишите программу, которая покажет большее и меньшее число. 
# В качестве символа-разделителя используйте пробел.

list_1 = list(map(int, input("Введите натуральные числа, используя пробел как разделитель:\n").split()))


max = list_1[0]
i = 0
for i in range(len(list_1)):
    if list_1[i] > max:
        max = list_1[i]


min = list_1[0]
i = 0
for i in range(len(list_1)):
    if list_1[i] < min:
        min = list_1[i]

print(max)
print(min)

