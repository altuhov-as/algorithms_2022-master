"""
Задание 2. Массив размером 2m + 1, где m – натуральное число,
заполнен случайным образом. Найдите в массиве медиану.

Медианой называется элемент ряда, делящий его на
две равные по длине части:
в одной находятся элементы,
которые не меньше медианы,
в другой – не больше медианы.

Решите задачу тремя способами:

1) с помощью сортировки, которую мы не рассматривали на уроке (Гномья, Шелла,
Кучей)

сделайте замеры на массивах длиной 10, 100, 1000 элементов
"""
import random
import timeit
from heapq import heappop, heappush

m = 1000
array = [random.randint(0, 500) for _ in range(2*m + 1)]
print('Исходный массив: {0}'.format(array))


def gnome_sort(ls):
    n, i = len(ls), 1
    while i < n:
        if ls[i - 1] <= ls[i]:
            i += 1
        else:
            ls[i - 1], ls[i] = ls[i], ls[i - 1]
            if i > 1:
                i -= 1
    return ls


def gnome_optimal(ls):
    i, j, size = 1, 2, len(ls)
    while i < size:
        if ls[i - 1] <= ls[i]:
            i, j = j, j + 1
        else:
            ls[i - 1], ls[i] = ls[i], ls[i - 1]
            i -= 1
            if i == 0:
                i, j = j, j + 1
    return ls


def shell(ls):
    inc = len(ls) // 2
    while inc:
        for i, el in enumerate(ls):
            while i >= inc and ls[i - inc] > el:
                ls[i] = ls[i - inc]
                i -= inc
            ls[i] = el
        inc = i if inc == 2 else int(inc*5.0/11)
    return ls


def heapsort(ls):
    heap = []
    for el in ls:
        heappush(heap, el)
    sort = []
    while heap:
        sort.append(heappop(heap))
    return sort


result = gnome_optimal(array[::])
# print('Отсортированный массив(gnome):\n{}'.format(gnome_sort(array[::])))
# print('Отсортированный массив(gnome оптимально):\n{}'.format(gnome_optimal(array[::])))
# print('Отсортированный массив(shell):\n{}'.format(shell(array[::])))
# print('Отсортированный массив(heap):\n{}'.format(heapsort(array[::])))

print('Медиана массива: {}'.format(result[m]))


print(
    timeit.timeit(
        "gnome_sort(array[::])",
        globals=globals(),
        number=100
    )
)
print(
    timeit.timeit(
        "gnome_optimal(array[::])",
        globals=globals(),
        number=100
    )
)
print(
    timeit.timeit(
        "shell(array[::])",
        globals=globals(),
        number=100
    )
)
print(
    timeit.timeit(
        "heapsort(array[::])",
        globals=globals(),
        number=100
    )
)
"""
На малых значениях разница не велика, на больших выигрывает сортировка Шелла и Кучей
Длинна массива: 21
0.0019463369999357383
0.0013939019995632407
0.0009176960002150736
0.0002999239995915559
Длинна массива: 201
0.31787617200006935
0.21338680300004853
0.030542931000127282
0.005526545000066108
Длинна массива: 2001
31.140960342999733
20.30993834899982
0.3596820910001952
0.07035149400007867
"""