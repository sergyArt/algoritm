# Python 3.6 x64
import sys

# 5. Вывести на экран коды и символы таблицы ASCII, начиная с символа под номером
# 32 и заканчивая 127-м включительно. Вывод выполнить в табличной форме: по десять пар "код-символ" в каждой строке.

for idx,i in enumerate(range(32,128)):
    if idx % 10 == 0:
        print('\n')
    print('[symbol: {}, cod: {}]  '.format(chr(i), i), end='')

print()
print(f'Выделено {sys.getsizeof(idx)}  байт на переменную idx')
print(f'Выделено {sys.getsizeof(i)}  байт на переменную i')



# 4. Определить, какое число в массиве встречается чаще всего.

def with_counter():
    mas = [10, 2, 8, 9, 10, 23, 45, 66, 10, 87, 2, 2, 2]
    max_elem = 0
    for i in mas:
        elem = mas.count(i)
        if elem > max_elem:
            max_elem = elem
            elem_value = i
    #print(elem_value, max_elem)

    print(f'Выделено {sys.getsizeof(mas)}  байт на переменную mas')
    print(f'Выделено {sys.getsizeof(max_elem)} байт на переменную elem')
    print(f'Выделено {sys.getsizeof(elem_value)} байт на переменную elem_value')
    print(f'Выделено {sys.getsizeof(i)} байт на переменную i')
    print(f'total {sys.getsizeof(mas) + sys.getsizeof(max_elem) + sys.getsizeof(elem_value) + sys.getsizeof(i) } байт')

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
    #print(max_elem, value_elem)
    print(f'Выделено {sys.getsizeof(mas)}  байт на переменную mas')
    print(f'Выделено {sys.getsizeof(max_elem)} байт на переменную elem')
    print(f'Выделено {sys.getsizeof(value_elem)} байт на переменную elem_value')
    print(f'Выделено {sys.getsizeof(value_next)} байт на переменную elem_next')
    print(f'Выделено {sys.getsizeof(i)} байт на переменную i')
    print(f'Выделено {sys.getsizeof(j)} байт на переменную j')
    print(f'total {sys.getsizeof(mas) + sys.getsizeof(max_elem) + sys.getsizeof(value_elem) + sys.getsizeof(i) + sys.getsizeof(value_next) + sys.getsizeof(j)} байт')


print('with_counter:')
with_counter()
print('without_counter:')
without_counter()

# Логичный результат, второй вариант потребляет больше памяти, так как имеет больше объявленных переменных

