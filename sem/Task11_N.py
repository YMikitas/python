# 1. Напишите программу, которая принимает на вход число N и выдаёт последовательность из N членов.    
#  Для N = 5: 1, -3, 9, -27, 81

list_random = []
number = int(input('Введите число N: '))

for i in range(0, number):
    list_random.append((-3)**i)
print(list_random)