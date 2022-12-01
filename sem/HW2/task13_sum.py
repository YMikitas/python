# 1 - Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр. Учтите, что числа могут быть отрицательными

# Пример:

# 67.82 -> 23
# (-0.56) -> 11

num = input('Введите вещественное число: ')

num = num.replace('-', '')

x = num.split(".") 
int_num = int(x[0])
fract_num = int(x[1])

result = 0

while (int_num != 0):
    result = result + (int_num % 10)
    int_num = int_num // 10

while (fract_num != 0):
    result = result + (fract_num % 10)
    fract_num = fract_num // 10

print(result)