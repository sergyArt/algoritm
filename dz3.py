# 1. В диапазоне натуральных чисел от 2 до 99 определить, сколько из них кратны каждому из чисел в диапазоне от 2 до 9.

l = [i for i in range(2, 100) for j in range(2, 10) if i % j == 0]

print(len(l))

# 2. Во втором массиве сохранить индексы четных элементов первого массива.
# Например, если дан массив со значениями 8, 3, 15, 6, 4, 2, то во второй
# массив надо заполнить значениями 1, 4, 5, 6 (или 0, 3, 4, 5 - если индексация
# начинается с нуля), т.к. именно в этих позициях первого массива стоят четные числа.

a = [2, 3, 8, 9, 10, 23, 45, 66, 68, 87]
b = []

[b.append(idx) for idx, i in enumerate(a) if i % 2 == 0]

print(b)

# 3. В массиве случайных целых чисел поменять местами минимальный и максимальный элементы.
import random
mas = [random.randint(1,100) for i in range(1, 10)]
print(mas, min(mas), max(mas))
idxmax = mas.index(max(mas))
idxmin = mas.index(min(mas))
if idxmax > idxmin:
    mas[mas.index(max(mas))], mas[mas.index(min(mas))] = mas[mas.index(min(mas))], mas[mas.index(max(mas))]
else:
    mas[mas.index(min(mas))], mas[mas.index(max(mas))] = mas[mas.index(max(mas))], mas[mas.index(min(mas))]
print(mas)

# 4. Определить, какое число в массиве встречается чаще всего.

mas = [10, 2, 8, 9, 10, 23, 45, 66, 10, 87]
print(mas)
max_elem = 0
for i in mas:
    elem = mas.count(i)
    if elem > max_elem:
        max_elem = elem
        elem_value = i
print(elem_value, max_elem)


# 5. В массиве найти максимальный отрицательный элемент. Вывести на экран его значение и позицию (индекс) в массиве.

mas = [10, -2, -8, 9, 10, 23, -45, 66, -10, -87]

print(min(mas), mas.index(min(mas)))

# 6. В одномерном массиве найти сумму элементов, находящихся между минимальным и максимальным элементами. Сами минимальный и максимальный элементы в сумму не включать.

mas = [random.randint(1,100) for i in range(1, 10)]

max_elem = max(mas)
min_elem = min(mas)
print(mas)
if mas.index(max_elem) > mas.index(min_elem):
    mas_copy = mas[mas.index(min_elem)+1:mas.index(max_elem)]
else:
    mas_copy = mas[mas.index(max_elem)+1:mas.index(min_elem)]

sum = 0
for i in mas_copy:
    sum += i

print(sum)

#7. В одномерном массиве целых чисел определить два наименьших элемента. Они могут быть как равны между собой (оба являться минимальными), так и различаться.

mas = [random.randint(1,100) for i in range(1, 10)]
print(mas)

mas.sort()
print(mas[:2])

# 8. Матрица 5x4 заполняется вводом с клавиатуры кроме последних элементов строк.
# Программа должна вычислять сумму введенных элементов каждой строки и записывать
# ее в последнюю ячейку строки. В конце следует вывести полученную матрицу.
# matr = []
# str_matr = []
# for i in range(1, 6):
#     str_matr = []
#     for j in range(1, 4):
#         j = input('Введите элемент матрицы:')
#         str_matr.append(j)
#     matr.append(str_matr)
# print(matr)
# for i in matr:
#     sum = 0
#     for j in i:
#         sum += int(j)
#     i.insert(3, sum)
#
# print(matr)




#9. Найти максимальный элемент среди минимальных элементов столбцов матрицы.

m = [['5', '4', '3'], ['7', '8', '6'], ['9', '8', '3'], ['1', '2', '3'], ['4', '5', '6']]
m1 = [list(x) for x in zip(*m)]
print(m)
print(m1)
min_elem_matr = []
for i in m1:
    min_elem_matr.append(min(i))
print(max(min_elem_matr))