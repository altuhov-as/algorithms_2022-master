"""
Задание 4.	Найти сумму n элементов следующего ряда чисел:
1 -0.5 0.25 -0.125 ...
Количество элементов (n) вводится с клавиатуры.

Пример:
Введите количество элементов: 3
Количество элементов - 3, их сумма - 0.75

Решите через рекурсию. Решение через цикл не принимается.
Нужно обойтисть без создания массива!
"""


def sum_row(n, result=0):
	n -= 1
	if n == 0:
		return result + 1
	result += 1/((-2)**n)
	return sum_row(n, result)


count = int(input("Введите количество элементов: "))
print(f"Количество элементов - {count}, их сумма - {sum_row(count)}")
