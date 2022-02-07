"""
Задание 1.

Приведен код, который позволяет сохранить в
массиве индексы четных элементов другого массива

Сделайте замеры времени выполнения кода с помощью модуля timeit

Попробуйте оптимизировать код, чтобы снизить время выполнения
Проведите повторные замеры

ОБЯЗАТЕЛЬНО! Добавьте аналитику: что вы сделали и какой это принесло эффект
"""

from timeit import timeit
import random

lst = []
for j in (50, 500, 1000, 5000, 10000):
    lst = random.sample(range(-100000, 100000), j)


def func_1(nums):
    new_arr = []
    for i in range(len(nums)):
        if nums[i] % 2 == 0:
            new_arr.append(i)
    return new_arr


def func_2(nums):
    return [k for k, v in enumerate(nums) if not v % 2]


NUMBER_EXECUTIONS = 1

time1 = timeit(f'func_1({lst})', setup='from __main__ import func_1', number=NUMBER_EXECUTIONS)

time2 = timeit(f'func_2({lst})', setup='from __main__ import func_2', number=NUMBER_EXECUTIONS)

print(time1)
print(time2)

"""
Вторая функция быстрее за счет использования встроенных функций получения элементов и 'генераторов списков'
"""
