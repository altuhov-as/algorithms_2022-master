"""
Задание 2.

Написать программу сложения и умножения двух шестнадцатеричных чисел.
При этом каждое число представляется как массив,
элементы которого это цифры числа.
Например, пользователь ввёл A2 и C4F.
Сохранить их как [‘A’, ‘2’] и [‘C’, ‘4’, ‘F’] соответственно.
Сумма чисел из примера: [‘C’, ‘F’, ‘1’],
произведение - [‘7’, ‘C’, ‘9’, ‘F’, ‘E’].

Подсказка:
Попытайтесь решить это задание в двух вариантах
1) через collections

defaultdict(list)
int(, 16)
reduce

2) через ООП

вспомните про перегрузку методов

__mul__
__add__
"""
from collections import deque, defaultdict
from functools import reduce


line1 = list("A2")
line2 = list("C4F")

dd = defaultdict(list)
dd.setdefault(0, line1)
dd.setdefault(1, line2)


def conv_hex(line: list):
    res = []
    for index, item in enumerate(reversed(line)):
        res.append(int(item, 16)*16**index)
    return reduce(lambda x, y: x + y, res)


result = []

for values in dd.values():
    result.append(conv_hex(values))

sum_all = reduce(lambda x, y: x + y, result)
dd.setdefault(len(dd), list(f'{sum_all:X}'))
print(f'Сумма двух чисел равна: {dd.popitem()[1]}')

mul_all = reduce(lambda x, y: x*y, result)
dd.setdefault(len(dd), list(f'{mul_all:X}'))
print(f'Поизведение двух чисел равно: {dd.popitem()[1]}')


class MyHex():
    _lst = []
    _line = ''

    def __init__(self, num: str):
        self._lst = [s for s in num]
        self._line = num

    def __mul__(self, other):
        if isinstance(other, MyHex):
            return list(f'{int(self._line, 16) * int(other._line, 16):X}')
        return False

    def __add__(self, other):
        if isinstance(other, MyHex):
            return list(f'{int(self._line, 16) + int(other._line, 16):X}')
        return False


first = MyHex("A2")
second = MyHex("C4F")
print("Результат через ООП:")
print(first + second)
print(first * second)
