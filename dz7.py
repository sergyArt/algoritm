# 1. Отсортируйте по убыванию методом "пузырька" одномерный целочисленный массив, заданный случайными числами на промежутке [-100; 100).
# Выведите на экран исходный и отсортированный массивы. Сортировка должна быть реализована в виде функции. По возможности доработайте алгоритм (сделайте его умнее).
import random
#
# def get_random_array(n):
#     return [random.randint(-100, 100) for _ in range(n)]
#
#
# def print_array(arr):
#     print(" ".join(map(str, arr)))
#
#
# arr = get_random_array(10)
#
#
# def sort_arr(arr):
#     for j in range(len(arr)):
#         for i in range(len(arr) - 1):
#             if arr[i] > arr[i + 1]:
#                 arr[i], arr[i + 1] = arr[i + 1], arr[i]
#
# print_array(arr)
# sort_arr(arr)
# print_array(arr)


# 2. Отсортируйте по возрастанию методом слияния одномерный вещественный массив, заданный случайными числами на промежутке [0; 50). Выведите на экран исходный и отсортированный массивы.


# arr = [random.randint(0, 50) for _ in range(10)]
#
# def quicksort(nums):
#    if len(nums) <= 1:
#        return nums
#    else:
#        q = random.choice(nums)
#    left_elements = [n for n in nums if n < q]
#    mid_elements = [q] * nums.count(q)
#    right_elements = [n for n in nums if n > q]
#
#    return quicksort(left_elements) + mid_elements + quicksort(right_elements)
#
#
# print_array(arr)
# print_array(quicksort(arr))


# 3. Массив размером 2m + 1, где m – натуральное число, заполнен случайным образом. Найдите в массиве медиану.
# Медианой называется элемент ряда, делящий его на две равные части: в одной находятся элементы, которые не меньше
# медианы, в другой – не больше медианы. Задачу можно решить без сортировки исходного массива. Но если это слишком сложно,
# то используйте метод сортировки, который не рассматривался на уроках

m = 3

arr = [random.randint(0,40) for _ in range(2*m + 1)]

print(arr)
med = 0
for i in arr:
    count = 0
    for j in arr:
        if j != i and j < i:
            count += 1
    if count == (len(arr) - 1) / 2:
        med = i


print('Медиана массива: ', med)