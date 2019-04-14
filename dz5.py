# 1. Пользователь вводит данные о количестве предприятий, их наименования и прибыль за 4 квартала (т.е. 4 отдельных числа) для каждого предприятия..
# Программа должна определить среднюю прибыль (за год для всех предприятий) и вывести наименования предприятий, чья прибыль выше среднего и отдельно
# вывести наименования предприятий, чья прибыль ниже среднего.
#
# from collections import defaultdict
# d = defaultdict(list)
#
# num = int(input("Value of organization:"))
# for i in range(1, num+1):
#     d[i].append(input('Info for production (name, p1, p2, p3, p4)').split())
#
# #print(d)
#
# pr_org = []
# avg_p = 0
# for i in d.keys():
#     sum = 0
#     for j in d[i][0][1:]:
#         sum += int(j)
#     avg_p += sum / len(d[i][0][1:])
#     pr_org.append([d[i][0][0], avg_p])
#
#
# print('AVG ALL: {}'.format(avg_p / len(d)))
# print('org pr less then average:')
# for i in pr_org:
#     if i[1] < avg_p / len(d):
#         print(i[0])
#
# print('org pr more then average:')
# for i in pr_org:
#     if i[1] > avg_p / len(d):
#         print(i[0])



# 2. Написать программу сложения и умножения двух шестнадцатеричных чисел. При этом каждое число представляется как массив, элементы
# которого это цифры числа. Например, пользователь ввёл A2 и C4F. Сохранить их как [‘A’, ‘2’] и [‘C’, ‘4’, ‘F’] соответственно.
# Сумма чисел из примера: [‘C’, ‘F’, ‘1’], произведение - [‘7’, ‘C’, ‘9’, ‘F’, ‘E’].

a = input('first number')
b = input('second number')
d = []
d.append(list(a))
d.append(list(b))
ad = '0x' + a
bd = '0x' + b
sum = int(ad,0) + int(bd,0)
mul = int(ad,0) * int(bd,0)
print('sum = ', hex(sum))
print('mul = ', hex(mul))

# Мне совершенно не понятно зачем в этой задаче использовать модуль collections.А если и попробовать, то не понятно какую коллекцию.