#Перечислить все положительные делители числа N

N = int(input("Введите число: "))
n = 1
nums = []
while n <= N:
    if N % n == 0:
        nums.append(n)
    n = n + 1
print(nums)