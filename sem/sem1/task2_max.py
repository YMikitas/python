# 2. Напишите программу, которая на вход принимает 5 чисел и находит максимальное из них.
#     Примеры:
#     - 1, 4, 8, 7, 5 -> 8
#     - 78, 55, 36, 90, 2 -> 90

nums = [4, 6, 8, 22, 77, 2]
maximum = nums[0]
for i in nums:
    if maximum < i:
        maximum = i
        
print (maximum)