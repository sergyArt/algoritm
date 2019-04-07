
# Сравнение скорости алгоритмов
# 4. Определить, какое число в массиве встречается чаще всего.

mas = [10, 2, 8, 9, 10, 23, 45, 66, 10, 87, 2, 2, 2]


def with_counter():
    mas = [10, 2, 8, 9, 10, 23, 45, 66, 10, 87, 2, 2, 2]
    max_elem = 0
    for i in mas:
        elem = mas.count(i)
        if elem > max_elem:
            max_elem = elem
            elem_value = i
    print(elem_value, max_elem)



def without_counter():
    mas = [10, 2, 8, 9, 10, 23, 45, 66, 10, 87, 2, 2, 2]
    max_elem = 0
    value_elem = 0
    for i in mas:
        next_elem = i
        value_next = 0
        for j in mas:
            if j == next_elem:
                value_next += 1
        if value_next > value_elem:
            max_elem = next_elem
            value_elem = value_next
        next_elem = 0
        value_next = 0
    print(max_elem, value_elem)


import timeit

print(timeit.timeit("with_counter()", setup="from __main__ import with_counter", number=1))
print(timeit.timeit("without_counter()", setup="from __main__ import without_counter", number=1))


# из проведенного опыта выходит что временные затраты на два вложенных прохода по списку, т.е O(n^2) быстрее чем использование встроенной функции count.
# Хотя чисто логически и там и там используется два прохода по одному и то му же списку

def my():
    num = 10
    m = [i for i in range(2, 1000)]
    number = 0
    for i in m:
        k = 2
        flag = True
        while k < i:
            if i % k == 0:
                flag = False
            k += 1
        if flag:
            number += 1
        if number == num:
            print(i)
            break


def alg():
    n = 1000
    resheto=[i for i in range(2,n) ]
    for j in range(0,len(resheto)):
        p=resheto[j]
        if p**2>n:
            break
        i=j+1
        while i<len(resheto):
            if resheto[i]%p==0:
                resheto.remove(resheto[i])
            i=i+1
    return resheto

#print(alg())
print(timeit.timeit("my()", setup="from __main__ import my", number=1))
print(timeit.timeit("alg()", setup="from __main__ import alg", number=1))

# временные показатели указывают на существенную сложность алгоритма решето Эратосфена


