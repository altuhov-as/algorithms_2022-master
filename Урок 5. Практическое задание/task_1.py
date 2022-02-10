# -*- coding: utf-8 -*-
"""
Задание 1.

Пользователь вводит данные о количестве предприятий,
их наименования и прибыль за 4 квартала
(т.е. 4 отдельных числа) для каждого предприятия.
Программа должна определить среднюю прибыль (за год для всех предприятий)
и вывести наименования предприятий, чья прибыль выше среднего и отдельно
вывести наименования предприятий, чья прибыль ниже среднего

Подсказка:
Для решения задачи обязательно примените коллекцию из модуля collections
Для лучшего освоения материала можете сделать
несколько варианто решения этого задания,
применив несколько коллекций из модуля collections

Пример:
Введите количество предприятий для расчета прибыли: 2
Введите название предприятия: Рога
через пробел введите прибыль данного предприятия
за каждый квартал(Всего 4 квартала): 235 345634 55 235

Введите название предприятия: Копыта
через пробел введите прибыль данного предприятия
за каждый квартал(Всего 4 квартала): 345 34 543 34

Средняя годовая прибыль всех предприятий: 173557.5
Предприятия, с прибылью выше среднего значения: Рога
Предприятия, с прибылью ниже среднего значения: Копыта
"""
import collections

Сompany = collections.namedtuple('Сompany', ['quarter1', 'quarter2', 'quarter3', 'quarter4', 'profit'])

base_enterprise = {}

total = 0
count = int(input("Количество предприятий: "))

for i in range(count):
    name = input(str(i+1) + '-е предприятие: ')
    lst = (input('Через пробел введите прибыль данного предприятия\
за каждый квартал(Всего 4 квартала): ').split(" "))
    lst = list(map(int, lst))
    profit_q1, profit_q2, profit_q3, profit_q4 = lst
    sum_y = sum(lst)
    total += sum_y
    base_enterprise[name] = Сompany(
        quarter1=profit_q1,
        quarter2=profit_q2,
        quarter3=profit_q3,
        quarter4=profit_q4,
        profit=sum_y
    )

base_enterprise["ROGA"] = Сompany(
        quarter1=100,
        quarter2=200,
        quarter3=300,
        quarter4=400,
        profit=1000
    )
total += base_enterprise["ROGA"].profit

base_enterprise["KOPITA"] = Сompany(
        quarter1=110,
        quarter2=220,
        quarter3=330,
        quarter4=440,
        profit=1100
    )
total += base_enterprise["KOPITA"].profit

total_avg = total / len(base_enterprise)
print(f'Средняя прибыль за год для всех предприятий {total_avg}')
lst_profit = []
lst_defit = []
for name, firm in base_enterprise.items():
    if firm.profit > total_avg:
        lst_profit.append(name)
    else:
        lst_defit.append(name)
print(f"Предприятия с прибылью выше средней {total_avg}: {', '.join(lst_profit)}.")
print(f"Предприятия с прибылью ниже средней {total_avg}: {', '.join(lst_defit)}.")
