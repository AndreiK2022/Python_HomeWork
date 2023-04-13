S = int(input("Задайте сумму чисел x и y: "))
P = int(input("Задайте произведение чисел x и y: "))

print(S, P)

end = 0
for i in range (1, 1001):
    if end != 1:
        for j in range (1, 1001):
            if end != 1:
                if i*j == P and i+j == S:
                    print("Загаданные числа:",i,"и",j)
                    end = 1