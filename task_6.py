"""
Задание 6.	В программе генерируется случайное целое число от 0 до 100.
Пользователь должен его отгадать не более чем за 10 попыток. После каждой
неудачной попытки должно сообщаться больше или меньше введенное пользователем
число, чем то, что загадано. Если за 10 попыток число не отгадано,
то вывести загаданное число.

Решите через рекурсию. Решение через цикл не принимается.
"""

import random

secret = random.randint(0, 100)
print(secret)

def get_answer(secret, current_step=1, count_step=10):
	if current_step == count_step:
		print f'Не угадано! Загаданное число {secret}'
	else:
		print(f'Попытка №{current_step:2} из {count_step}')
		user_number = int(input('Введите число от 1 до 100: '))
		if user_number == secret:
			print('Загаданное число угадано')
			return
		elif user_number > secret:
			print(f'Ваше число {user_number} больше загаданного')
		else:
			print(f'Ваше число {user_number} меньше загаданного')
		current_step += 1
		get_answer(secret, current_step)


get_answer(secret)