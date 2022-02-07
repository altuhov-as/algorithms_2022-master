"""
Задание 3.

Приведен код, формирующий из введенного числа
обратное по порядку входящих в него
цифр и вывести на экран.

Сделайте профилировку каждого алгоритма через timeit

Обязательно предложите еще свой вариант решения!

Сделайте вывод, какая из четырех реализаций эффективнее и почему!!!
"""
from timeit import timeit


def revers(enter_num, revers_num=0):
    if enter_num == 0:
        return
    else:
        num = enter_num % 10
        revers_num = (revers_num + num / 10) * 10
        enter_num //= 10
        revers(enter_num, revers_num)


def revers_2(enter_num, revers_num=0):
    while enter_num != 0:
        num = enter_num % 10
        revers_num = (revers_num + num / 10) * 10
        enter_num //= 10
    return revers_num


def revers_3(enter_num):
    enter_num = str(enter_num)
    revers_num = enter_num[::-1]
    return revers_num


def revers_4(enter_num):
    enter_num = str(enter_num)
    return "".join(reversed(enter_num))


num_ = 1234567890987654321

print(
    timeit(
        "revers(num_)",
        setup='from __main__ import revers, num_',
        number=10000))

print(
    timeit(
        "revers_2(num_)",
        setup='from __main__ import revers_2, num_',
        number=10000))

print(
    timeit(
        "revers_3(num_)",
        setup='from __main__ import revers_3, num_',
        number=10000))

print(
    timeit(
        "revers_4(num_)",
        setup='from __main__ import revers_4, num_',
        number=10000))

"""
Срез — самый быстрый подход, reversed() медленнее среза в 8 раз,
 и «классический» алгоритм медленнее в 71 раз в этой проверке!
"""