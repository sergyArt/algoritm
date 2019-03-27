# # 1. Найти сумму и произведение цифр трехзначного числа, которое вводит пользователь.
num = input("Введите число")
sum = 0
pr = 1
for i in num:
    sum += int(i)
    pr *= int(i)

print("sum = ", sum, "pr = ", pr)
#
# #2. Выполнить логические побитовые операции «И», «ИЛИ» и др. над числами 5 и 6.
# # Выполнить над числом 5 побитовый сдвиг вправо и влево на два знака.
# # Объяснить полученный результат.

a = 5
b = 6

print("число 5: ", bin(a))
print("число 6: ", bin(b))3
print("or", bin(a | b))
print("and", bin(a & b))
print("xor", bin(a ^ b))
print(">>", bin(a >> 2))

# #3. По введенным пользователем координатам двух точек вывести уравнение прямой вида y=kx+b,
# # проходящей через эти точки.
#
x1 = int(input("Введите координату х первого числа:"))
y1 = int(input("Введите координату y первого числа:"))
x2 = int(input("Введите координату х второго числа:"))
y2 = int(input("Введите координату y второго числа:"))

k = (y2-y1)/(x2-x1)
c = (y2*x1 - y1*x2)/(x2-x1)

print("y=", k, "x + (", c, ")")

#4. Написать программу, которая генерирует в указанных пользователем границах:
# случайное целое число;
# случайное вещественное число;
# случайный символ.
# Для каждого из трех случаев пользователь задает свои границы диапазона.
# Например, если надо получить случайный символ от 'a' до 'f', то вводятся эти символы.
# Программа должна вывести на экран любой символ алфавита от 'a' до 'f' включительно.
#
import random
x = int(input("Введите левую границу:"))
y = int(input("Введите правую границу:"))

print("random int:", random.randint(x,y))
print("random decimal:", random.uniform(x,y))
xs = input("Введите первый символ:")
ys = input("Введите последний символ:")
print("random symbol:", chr(random.randint(ord(xs), ord(ys))))

# # 5. Пользователь вводит две буквы.
# # Определить, на каких местах алфавита они стоят и сколько между ними находится букв.
import string
cxm = 0
cym = 0
s_al =  string.ascii_letters[:26]
cx = input("Введите первую букву:")
cy = input("Введите последнюю букву:")
for idx,i in enumerate(s_al):
    if i == cx:
        cxm = idx + 1
    elif i == cy:
        cym = idx + 1
print("Места в алфавите: ", cxm, cym, "между ними ", cym-cxm-1 if cxm < cym else cxm-cym-1, "букв")

#6. Пользователь вводит номер буквы в алфавите. Определить, какая это буква.
num_chr = int(input("Введите номер буквы:"))
for idx,i in enumerate(s_al):
    if idx == num_chr-1:
        print("Буква: ", i)
        break;

# 7. По длинам трех отрезков, введенных пользователем, определить возможность существования
# треугольника, составленного из этих отрезков. Если такой треугольник существует, то определить,
# является ли он разносторонним, равнобедренным или равносторонним.
ab = int(input('Введите длину отрезка ab'))
bc = int(input('Введите длину отрезка bc'))
ca = int(input('Введите длину отрезка ca'))

if (ab+bc > ca) and (bc+ca > ab) and (ca+ab > bc):
    if ab == bc == ca:
        print('равносторонний треугольник')
    else:
        print('неравносторонний треугольник')
else:
    print('нет треугольника')



year = int(input('Введите год: '))

if year % 4 != 0 or (year % 100 == 0 and year % 400 !=0):
    print('Не високосный')
else:
    print('Високосный')


a = int(input('Введите число a: '))
b = int(input('Введите число b: '))
c = int(input('Введите число c: '))

if a>b and a<c:
    print('a в центре')
elif b>a and b<c:
    print('b в центре')
else:
    print('c в центре')


l = []
with open('passlog.txt','r') as f:
    for line in f:
        l.append(((line.split(sep=';'))[1]).replace('\n',''))
from collections import Counter
print(Counter(l).most_common(10))

import random
k = 5
f = False
res = random.randint(1,11)
for i in range(1, k+1):
    nam = int(input('Введите ччисло:'))
    if nam == res:
        print('Вы выиграли!')
        f = True
        break
    elif nam>res:
        print('Слишком большое число')
    else:
        print('Слишком маленькое число')
if f == False:
    print('Вы проиграли')

