"""
Задача 3.
В соответствии с документацией Python,
deque – это обобщение стеков и очередей.
Вот основное правило: если вам нужно
что-то быстро дописать или вытащить, используйте deque.
Если вам нужен быстрый случайный доступ, используйте list

Задача: создайте простой список (list) и очередь (deque).
Выполните различные операции с каждым из объектов.
Сделайте замеры и оцените, насколько информация в документации
соответствует дейстивтельности.

1) сравнить операции
append, pop, extend списка и дека и сделать выводы что и где быстрее

2) сравнить операции
appendleft, popleft, extendleft дека и соответствующих им операций списка
и сделать выводы что и где быстрее

3) сравнить операции получения элемента списка и дека
и сделать выводы что и где быстрее

Подсказка:
для того, чтобы снизить погрешность, желательно операции по каждой ф-ции
(append, pop и т.д.) проводить в циклах. Для замеров используйте timeit.
"""
from collections import deque
from timeit import timeit
import random


lst = []
deq = deque()

for j in range(500):
    ext_lst = random.sample(range(0, 1000), j)

size_lst = 1000
size_pop = int(size_lst/10)

for j in range(300):
    get_lst = random.sample(range(0, 300), j)


def app_l(count: int):
    for i in range(count):
        lst.append(i)


def app_d(count: int):
    for i in range(count):
        deq.append(i)


def pop_l(count_pop: int):
    for i in range(count_pop):
        lst.pop()


def pop_d(count_pop: int):
    for i in range(count_pop):
        deq.pop()


def extend_l(ext):
    lst.extend(ext)


def extend_d(ext):
    deq.extend(ext)


def append_left_l():
    for i in range(10):
        lst.insert(0, i)


def append_left_d():
    for i in range(10):
        deq.appendleft(i)


def popleft_l():
    for i in range(50):
        lst.pop(0)


def popleft_d():
    for i in range(50):
        deq.popleft()


def get_item_l(get_l):
    for g in get_l:
        yield lst[g]


def get_item_d(get_l):
    for g in get_l:
        yield deq[g]


print(
    timeit(
        "app_l(size_lst)",
        setup='from __main__ import app_l, size_lst',
        number=10000))

print(
    timeit(
        "app_d(size_lst)",
        setup='from __main__ import app_d, size_lst',
        number=10000))
print("appended")
print(
    timeit(
        "pop_l(size_pop)",
        setup='from __main__ import pop_l, size_pop',
        number=10000))

print(
    timeit(
        "pop_d(size_pop)",
        setup='from __main__ import pop_d, size_pop',
        number=10000))
print("popped")
print(
    timeit(
        "extend_l(ext_lst)",
        setup='from __main__ import extend_l, ext_lst',
        number=10000))

print(
    timeit(
        "extend_d(ext_lst)",
        setup='from __main__ import extend_d, ext_lst',
        number=10000))
print("extended")
print(
    timeit(
        "append_left_l()",
        setup='from __main__ import append_left_l',
        number=10))

print(
    timeit(
        "append_left_d()",
        setup='from __main__ import append_left_d',
        number=10))
print("appended left")
print(
    timeit(
        "popleft_l()",
        setup='from __main__ import popleft_l',
        number=10))

print(
    timeit(
        "popleft_d()",
        setup='from __main__ import popleft_d',
        number=10))
print("popped left")
print(
    timeit(
        "get_item_l(get_lst)",
        setup='from __main__ import get_item_l, get_lst',
        number=10000))

print(
    timeit(
        "get_item_d(get_lst)",
        setup='from __main__ import get_item_d, get_lst',
        number=10000))
print("getted value")

"""
0.3812025810002524
0.39145912200183375
appended
0.03086154100310523
0.03138692200082005
popped
0.01244872499955818
0.02179439999963506
extended
1.5357651010017435          список проигрывает при добавлении элементов слева
1.0150000889552757e-05
appended left
6.928675230999943           список проигрывает при удалении элементов слева
3.7898000300629064e-05
popped left
0.00171737499840674
0.0015689009997004177
getted value


ВЫРАЖЕНИЕ ВЕРНО: что-то быстро дописать или вытащить, используйте deque.

Список хранит элементы рядом друг с другом и использует непрерывную память. Это наиболее эффективно для нескольких
операций, таких как индексация в списке. Например, получение list1 [2] выполняется быстро, поскольку Python знает
 точное положение определенного элемента. Непрерывная память также позволяет хорошо работать со списками.
Список требует больше времени, чтобы добавить некоторые объекты, чем другие. Если блок непрерывной памяти заполнен,
 он получит другой блок, который может занять гораздо больше времени, чем обычная функция append().
"""