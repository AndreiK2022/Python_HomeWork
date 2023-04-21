# Согласно условию, грядка задана в доп. файле bed. Количество кустов задано,
# а количество ягод на каждом кусте задается рандомом.

import bed

list = []
sum_berries = 0
for i in range (1, bed.N+1):
    if i == 1:
        sum_berries = bed.bed[i] + bed.bed[bed.N] + bed.bed[i+1]
        list.append(sum_berries)
        i = i+1
    else:
        if i == bed.N:
            sum_berries = bed.bed[i] + bed.bed[1] + bed.bed[i-1]
            list.append(sum_berries)
        else:
            sum_berries = bed.bed[i] + bed.bed[i-1] + bed.bed[i+1]
            list.append(sum_berries)
            i = i+1
print(list)
print("Максимальное количество ягод за один заход :",max(list))