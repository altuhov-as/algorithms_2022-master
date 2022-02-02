"""
Задание 1.

Реализуйте:

a) заполнение списка, оцените сложность в O-нотации.
   заполнение словаря, оцените сложность в O-нотации.
   сделайте аналитику, что заполняется быстрее и почему.
   сделайте замеры времени.

b) выполните со списком и словарем операции: изменения и удаления элемента.
   оцените сложности в O-нотации для операций
   получения и удаления по списку и словарю
   сделайте аналитику, какие операции быстрее и почему
   сделайте замеры времени.


ВНИМАНИЕ: в задании два пункта - а) и b)
НУЖНО выполнить оба пункта

Подсказка: для замеров воспользуйтесь модулем time (см. примеры урока 1)
вы уже знаете, что такое декоратор и как его реализовать,
обязательно реализуйте ф-цию-декоратор и пусть она считает время
И примените ее к своим функциям!
"""
import random
import time


def time_of_function(function):
    def wrapper(*args):
        start_val = time.time()
        function(*args)
        end_val = time.time()
        time_funk = end_val - start_val
        return time_funk
    return wrapper


my_list = []
my_dict = {}


@time_of_function
def list_app(i=1):
    for i in range(i):
        my_list.append(random.choice(range(1000, 10000000000))) #O(1)
    for i in range(i//1000):
        my_list[i] += 1                                         #O(1)
    for i in range(i//1000):
        my_list.pop()                                           #O(1)
    return my_list


@time_of_function
def dict_app(i=1):
    for i in range(i):
        my_dict[i] = (random.choice(range(1000, 10000000000)))  #O(1)
    for i in range(i//1000):
        my_dict[i] = 1                                          #O(1)
    for i in range(i//1000):
        my_dict.popitem()                                       #O(1)
    return my_dict


"""
для наглядности выполнить 5 сравнений времени
"""
result = []
for j in range(5):
    time_l, time_d = list_app(100000), dict_app(100000)
    print(time_l, time_d)
    result.append(time_l < time_d)

print(all(result))

"""
Время выполнения добавления элементов в словарь больше, чем в список,
из-за расчёта хеша для эллементов. 
"""
