"""
Задание 4.

Приведены два алгоритма. В них определяется число,
которое встречается в массиве чаще всего.

Сделайте профилировку каждого алгоритма через timeit

Обязательно напишите третью версию (здесь возможно даже решение одной строкой).
Сделайте замеры и опишите, получилось ли у вас ускорить задачу.
"""
from timeit import timeit

array = [1, 3, 1, 3, 4, 5, 1]


def func_1():
    m = 0
    num = 0
    for i in array:
        count = array.count(i)
        if count > m:
            m = count
            num = i
    return f'Чаще всего встречается число {num}, ' \
           f'оно появилось в массиве {m} раз(а)'


def func_2():
    new_array = []
    for el in array:
        count2 = array.count(el)
        new_array.append(count2)

    max_2 = max(new_array)
    elem = array[new_array.index(max_2)]
    return f'Чаще всего встречается число {elem}, ' \
           f'оно появилось в массиве {max_2} раз(а)'


def func_3():
    res = max({i: array.count(i) for i in array}.items(), key=lambda i: i[1])
    return f'Чаще всего встречается число {res[0]}, ' \
           f'оно появилось в массиве {res[1]} раз(а)'


def func_4():
    max_index = 0
    for i in array:
        if array.count(max_index) < array.count(i):
            max_index = array.index(i)

    return f'Число {array[max_index]}, встречается {array.count(max_index)} раза'


def func_5():
    income = {i: array.count(i) for i in array}
    v = list(income.values())
    k = list(income.keys())
    return k[v.index(max(v))]


def func_6():
    res = max(map(lambda val: (array.count(val), val), set(array)))
    return f'Чаще всего встречается число {res[0]}, ' \
           f'оно появилось в массиве {res[1]} раз(а)'


print(func_6())

print(
    timeit(
        "func_1()",
        setup='from __main__ import func_1, array',
        number=10000))

print(
    timeit(
        "func_2()",
        setup='from __main__ import func_2, array',
        number=10000))

print(
    timeit(
        "func_3()",
        setup='from __main__ import func_3, array',
        number=10000))

print(
    timeit(
        "func_4()",
        setup='from __main__ import func_4, array',
        number=10000))

print(
    timeit(
        "func_5()",
        setup='from __main__ import func_5, array',
        number=10000))

print(
    timeit(
        "func_6()",
        setup='from __main__ import func_6, array',
        number=10000))

"""
По результатам замеров не получилось ускорить задачу.
P.S.: шестая функция сама быстрая, до введения     'return f'Чаще всего встречается число {res[0]}, ' \
           f'оно появилось в массиве {res[1]} раз(а)'', после отого стала второй по скорости
"""