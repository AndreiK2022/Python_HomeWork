# Дана последовательность натуральных чисел (одно число в строке), завершающаяся числом 0.
# Определите значение второго по величине элемента в этой последовательности, то есть элемента, который будет
# наибольшим, если из последовательности удалить наибольший элемент.
# В этой задаче нельзя использовать глобальные переменные. Функция получает данные, считывая их с клавиатуры,
# а не получая их в виде параметра. В программе на языке Python функция возвращает результат в виде кортежа из
# нескольких чисел и функция вообще не получает никаких параметров. 

def tup(string):
    arr = []
    while (x := int(input(string))):
        arr.append(x)
    arrTup = tuple(arr)    
    return sorted(arrTup)

print (tup("Введите значение: ")[-2])

