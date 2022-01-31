"""
Задание 7.	Напишите программу, доказывающую или проверяющую, что для множества
натуральных чисел выполняется равенство: 1+2+...+n = n(n+1)/2,
где n - любое натуральное число.

Пример:
для n = 5
1+2+3+4+5 = 5(5+1)/2

Нужно написать функцибю-рекурсию только для левой части выражения!
Результат нужно сверить с правой частью.

Решите через рекурсию. Решение через цикл не принимается.
"""


def control_sum(n: int):
	if n < 2:
		return 1
	else:
		return n + control_sum(n - 1)


def formula(n):
	return n*((n+1)/2)


number = 6
print(control_sum(number) == formula(number))

