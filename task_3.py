"""
Задание 3.	Сформировать из введенного числа
обратное по порядку входящих в него
цифр и вывести на экран. Например, если введено число 3486,
то надо вывести число 6843.

Подсказка:
На каждом шаге вам нужно 'доставать' из числа очередную цифру
Пока все числа не извлечены рекурсивные вызовы продолжаем
Условие завершения рекурсии - все цифры извлечены
Используем операции % //. Операции взятия по индексу применять нельзя.

Решите через рекурсию. Решение через цикл не принимается.

Пример:
Введите число, которое требуется перевернуть: 123
Перевернутое число: 321
Не забудьте проверить на числе, которое оканчивается на 0.
1230->3210
"""

result = ""


def reverse_num(n : int, zero=False):
	global result
	if len( str(n) ) == 1:
		result+= str(n%10)
		if zero:
			result+='0'
		return
	if n%10 == 0:
		zero = True
		reverse_num(n//10, zero)
	else:
		result+=( str(n%10) )
		reverse_num(n//10, zero)


reverse_num( int( input("Input integer number: ")) )

print(result)