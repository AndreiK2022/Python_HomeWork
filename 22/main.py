import random

m = int(input("Введите количество элементов первого набора чисел: "))
n = int(input("Введите количество элементов второго набора чисел: "))
print(m, n)

m_list = []
n_list = []

for i in range(m):
    m_list.append(random.randint(-10, 10))
    i = i+1

for j in range(n):
    n_list.append(random.randint(-10, 10))
    i = i+1

print(m_list)
print(n_list)

set_m = set(m_list)
set_n = set(n_list)
o = sorted(set_m.intersection(set_n))
str_o = [str(k) for k in o]                      # для вывода без []
print(', '.join(str_o))