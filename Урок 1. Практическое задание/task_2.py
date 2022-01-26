#-*- coding: utf-8 -*-

"""
Задание 2.

Реализуйте два алгоритма.

Оба должны обеспечивать поиск минимального значения для списка.

Сложность первого алгоритма должна быть O(n^2) - квадратичная.

Сложность второго алгоритма должна быть O(n) - линейная.


Примечание: ПРОШУ ВАС ВНИМАТЕЛЬНО ЧИТАТЬ ЗАДАНИЕ!
-- нельзя использовать встроенные функции min() и sort()
"""


# сложность O(n)
def first_min(lst):        
    result = lst[0]         # O(1)
    for i in lst:           # O(n)
        if i < result:      # O(1)
            result = i      # O(1)
    return result           # O(1)


# сложность O(n**2)
def second_min(lst):
    result = lst[0]                     # O(1)
    for i in range(len(lst) - 1):       # O(n)
        for j in range(i+1, len(lst)):  # O(n)
            if j < result:              # O(len(i)
                result = lst[j]              # O(1)
    return result                       # O(1)


my_lst = [10, 7, 5, 2, 6, 9]

print(first_min(my_lst))
print(second_min(my_lst))
