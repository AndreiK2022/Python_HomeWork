# Петя, Катя и Сережа делают из бумаги журавликов. Вместе они сделали S журавликов.
# Сколько журавликов сделал каждый ребенок, если известно, что Петя и Сережа сделали одинаковое количество журавликов,
# а Катя сделала в два раза больше журавликов, чем Петя и Сережа вместе?

# *Пример:*

# 6 -> 1  4  1
# 24 -> 4  16  4
# 60 -> 10  40  10

S = int(input("Введите общее количество журавликов: "))
a = S%6
if a == 0:
    print(S//6, S//6, (S//6+S//6)*2)
else:
    print(round(S/6, 1), round(S/6, 1), round((S/6+S/6)*2, 1))