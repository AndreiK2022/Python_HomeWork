# Требуется вывести все целые степени двойки (т.е. числа вида 2k), не превосходящие числа N.

N = int(input("Введите число: "))

k = 1
while 2**k < N:
    print(2**k)
    k = k + 1