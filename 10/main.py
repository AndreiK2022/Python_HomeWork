import random

n = int(input("Задайте количество монет: "))
coins = []

for _ in range (n):
    coins.append(random.randint(0, 1))
print(coins)

i = 0
side0 = 0
side1 = 0
while i < n:
    if coins[i] == 0:
        side0 = side0 + 1
        i = i+1
    else:
        side1 = side1 + 1
        i = i+1
print(side0, side1)

if side0 > side1:
    print("Нужно перевернуть",side1,"монет")
else:
    print("Нужно перевернуть",side0,"монет")
