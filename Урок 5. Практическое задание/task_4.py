"""
Задача 4.
Создайте обычный словарь и упорядоченный словарь OrderedDict.

Выполните операции, равные по смыслу, с каждым из словарей и сделайте замеры.
Опишите полученные результаты, сделайте выводы

И есть ли смысл исп-ть OrderedDict в Python 3.6 и более поздних версиях
"""

import random
from collections import OrderedDict
from timeit import timeit

lst = []
for j in range(5000):
    lst = random.sample(range(0, 10000), j)

d = {}
od = OrderedDict()


def generate_d():
    return {k: v for k, v in enumerate(lst)}


def add_d(l: list):
    for k, v in enumerate(l):
        d[k] = v


def add_od(l: list):
    for k, v in enumerate(l):
        od[k] = v


def change_d():
    for i in range(1000):
        d[i] = i + 1


def change_od():
    for i in range(1000):
        od[i] = i + 1


def pop_d():
    for i in range(1000):
        d.pop(i)


def pop_od():
    for i in range(1000):
        od.pop(i)


def popitem_d():
    for i in range(1000):
        d.popitem()


def popitem_od():
    for i in range(1000):
        od.popitem()


add_d(lst)
add_od(lst)

print(
    timeit(
        "add_d(lst)",
        setup='from __main__ import add_d, lst',
        number=10000))

print(
    timeit(
        "add_od(lst)",
        setup='from __main__ import add_od, lst',
        number=10000))
print("added")
print(
    timeit(
        "change_d()",
        setup='from __main__ import change_d',
        number=10000))

print(
    timeit(
        "change_od()",
        setup='from __main__ import change_od',
        number=10000))
print("changed")
print(
    timeit(
        "pop_d()",
        setup='from __main__ import pop_d',
        number=1))

print(
    timeit(
        "pop_od()",
        setup='from __main__ import pop_od',
        number=1))
print("popped")
print(
    timeit(
        "popitem_d()",
        setup='from __main__ import popitem_d',
        number=3))

print(
    timeit(
        "popitem_od()",
        setup='from __main__ import popitem_od',
        number=3))
print("popped item")
"""
3.3846088950012927
3.9972516570014704          OrderedDict проигрывает по времени в добавлении элементов
added
0.5632874580005591
1.1370635769999353          OrderedDict проигрывает по времени в изменении элементов
changed
0.00010591699901851825
0.00020415800099726766
popped
0.0003234550022170879
0.00034405200131004676
popped item

OrderedDict всё ещё ценный и отличающимся от обычного dict:

Сигнализация намерения: если вы используете OrderedDictвместо dict , тогда ваш код проясняет,
что важен порядок элементов в словаре. Вы чётко даёте понять, что вашему коду нужен порядок элементов в базовом словаре
или он полагается на него. Контроль над порядком элементов: если вам нужно переставить или переупорядочить элементы
в словаре, вы можете использовать .move_to_end() , а также расширенный вариант .popitem() .
Проверка на равенство: если ваш код сравнивает словари на предмет равенства, и порядок элементов важен в этом сравнении,
то OrderedDict правильный выбор.

"""