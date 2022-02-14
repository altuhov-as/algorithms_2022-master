"""
Задание 1.

Вам нужно взять 5 любых скриптов, написанных ВАМИ в рамках работы над ДЗ
курсов Алгоритмы и Основы Python

На каждый скрипт нужно два решения - исходное и оптимизированное.

Вы берете исходное, пишете что это за задание и с какого оно курса.
Далее выполняете профилирование скрипта средствами memory_profiler

Вы оптимизируете исходное решение.
Далее выполняете профилирование скрипта средствами memory_profiler

Вам нужно написать аналитику, что вы сделали для оптимизации памяти и
чего добились.


ВНИМАНИЕ:
1) скрипты для оптимизации нужно брать только из сделанных вами ДЗ
курсов Алгоритмы и Основы
2) нельзя дублировать, коды, показанные на уроке
3) для каждого из 5 скриптов у вас отдельный файл, в нем должна быть версия до
и версия после оптимизации
4) желательно выбрать те скрипты, где есть что оптимизировать и не брать те,
где с памятью и так все в порядке
5) не нужно писать преподавателю '''я не могу найти что оптимизировать''', это
отговорки. Примеров оптимизации мы перечислили много: переход с массивов на
генераторы, numpy, использование слотов, применение del, сериализация и т.д.

Это файл для четвертого скрипта
"""
from memory_profiler import profile


@profile
def my_code(line):
    user_list = line.split()
    my_list = []

    for i in range(len(user_list)):
        my_list.append(None)

    if len(user_list) % 2 == 0:
        for i, v in enumerate(user_list):
            if i % 2 == 1:
                my_list[i - 1] = v
                my_list[i] = user_list[i - 1]
    else:
        for i, v in enumerate(user_list):
            if i % 2 == 1:
                my_list[i - 1] = v
                my_list[i] = user_list[i - 1]
            elif i == len(user_list) - 1:
                my_list[i] = v

    print(my_list)


@profile
def optimal(line):
    my_list = line.split()
    print('Введеный список: ', my_list)

    idx = len(my_list) if len(my_list) % 2 == 0 else len(my_list) - 1

    my_list[:idx:2], my_list[1:idx:2] = my_list[1:idx:2], my_list[:idx:2]
    print('Измененный список: ', my_list)


example = "1 2 3 4 5 6 7 8 9 10 12 23 45 34 56 78 89 13 45 78 90"


if __name__ == "__main__":
    my_code(example)
    optimal(example)

"""
Основы языка Python
Лекция 2. Задача 2. Для списка реализовать обмен значений соседних элементов, т.е. Значениями обмениваются элементы
 с индексами 0 и 1, 2 и 3 и т.д. При нечетном количестве элементов последний сохранить на своем месте.
Для заполнения списка элементов необходимо использовать функцию input().


Избавился от первого спика, в оптимизированном коде используется только один список. Не создаю enumerate
Line #    Mem usage    Increment  Occurrences   Line Contents
=============================================================
    36     17.8 MiB     17.8 MiB           1   @profile
    37                                         def my_code(line):
    38     17.8 MiB      0.0 MiB           1       user_list = line.split()
    39     17.8 MiB      0.0 MiB           1       my_list = []
    40                                         
    41     17.8 MiB      0.0 MiB          22       for i in range(len(user_list)):
    42     17.8 MiB      0.0 MiB          21           my_list.append(None)
    43                                         
    44     17.8 MiB      0.0 MiB           1       if len(user_list) % 2 == 0:
    45                                                 for i, v in enumerate(user_list):
    46                                                     if i % 2 == 1:
    47                                                         my_list[i - 1] = v
    48                                                         my_list[i] = user_list[i - 1]
    49                                             else:
    50     17.8 MiB      0.0 MiB          22           for i, v in enumerate(user_list):
    51     17.8 MiB      0.0 MiB          21               if i % 2 == 1:
    52     17.8 MiB      0.0 MiB          10                   my_list[i - 1] = v
    53     17.8 MiB      0.0 MiB          10                   my_list[i] = user_list[i - 1]
    54     17.8 MiB      0.0 MiB          11               elif i == len(user_list) - 1:
    55     17.8 MiB      0.0 MiB           1                   my_list[i] = v
    56                                         
    57     17.8 MiB      0.0 MiB           1       print(my_list)
    
    
    60     17.6 MiB     17.6 MiB           1   @profile
    61                                         def optimal(line):
    62     17.6 MiB      0.0 MiB           1       my_list = line.split()
    63     17.6 MiB      0.0 MiB           1       print('Введеный список: ', my_list)
    64                                         
    65     17.6 MiB      0.0 MiB           1       idx = len(my_list) if len(my_list) % 2 == 0 else len(my_list) - 1
    66                                         
    67     17.6 MiB      0.0 MiB           1       my_list[:idx:2], my_list[1:idx:2] = my_list[1:idx:2], my_list[:idx:2]
    68     17.6 MiB      0.0 MiB           1       print('Измененный список: ', my_list)

"""