"""
Задание 5.**

Приведен наивный алгоритм нахождения i-го по счёту
простого числа (через перебор делителей).

Попробуйте решить эту же задачу,
применив алгоритм "Решето Эратосфена" (в материалах есть его описание)

Подсказка:
Сравните алгоритмы по времени на разных порядковых номерах чисел:
10, 100, 1000
Опишите результаты, сделайте выводы, где и какой алгоритм эффективнее
"""
from builtins import enumerate
from timeit import timeit


def simple(i):
    """Без использования «Решета Эратосфена»"""
    count = 1
    n = 2
    while count <= i:
        t = 1
        is_simple = True
        while t <= n:
            if n % t == 0 and t != 1 and t != n:
                is_simple = False
                break
            t += 1
        if is_simple:
            if count == i:
                break
            count += 1
        n += 1
    return n


i = int(input('Введите порядковый номер искомого простого числа: '))
print(simple(i))

lst = {}


def sieve(count_n: int):
    if count_n == 1:
        return 2
    sie = set(range(2, count_n + 1))
    while sie:
        prime = min(sie)
        sie -= set(range(prime, count_n, prime))
        yield prime


def my_sieve(start: int, fin: int):
    sie = set(range(start, fin + 1))
    while sie:
        prime = min(sie)
        sie -= set(range(prime, fin + 1, prime))
        if prime not in lst.values():
            lst[len(lst) + 1] = prime


def sieve_lst(n: int):
    my_sieve(2, 100)
    if n < len(lst):
        return lst.get(n)
    else:
        p = 0
        while n > len(lst):
            my_sieve(2, n*(10**p))
            p += 1
        return lst.get(n)


print(sieve_lst(i))

print(
    timeit(
        "sieve_lst(i)",
        setup='from __main__ import sieve_lst, i',
        number=10000))
print(
    timeit(
        "simple(i)",
        setup='from __main__ import simple, i',
        number=10000))

"""
предложенное мною решение превосходит предложенное уже с 18 простого числа. На первых 17 проигрывает по времени
"""
