# Напишите программу, которая на вход принимает два числа A и B,
# и возводит число А в целую степень B с помощью рекурсии.

A = int(input("Введите число A: "))
B = int(input("Введите число B: "))

def stepen(m, n):
    if (n == 1):
        return (m)
    if (n != 1):
        return (m * stepen(m, n - 1))

print(stepen(A, B))