"""
Задание 1.	Написать программу, которая будет складывать, вычитать,
умножать или делить два числа. Числа и знак операции вводятся пользователем.
После выполнения вычисления программа не должна завершаться, а должна
запрашивать новые данные для вычислений. Завершение программы должно
выполняться при вводе символа '0' в качестве знака операции. Если пользователь
вводит неверный знак (не '0', '+', '-', '*', '/'), то программа должна
сообщать ему об ошибке и снова запрашивать знак операции.

Также сообщать пользователю о невозможности деления на ноль,
если он ввел 0 в качестве делителя.

Подсказка:
Вариант исполнения:
- условие рекурсивного вызова - введена операция +, -, *, / - ШАГ РЕКУРСИИ
- условие завершения рекурсии - введена операция 0 - БАЗОВЫЙ СЛУЧАЙ

Решите через рекурсию. Решение через цикл не принимается.

Пример:
Введите операцию (+, -, *, / или 0 для выхода): +
Введите первое число: 214
Введите второе число: 234
Ваш результат 448
Введите операцию (+, -, *, / или 0 для выхода): -
Введите первое число: вп
Вы вместо трехзначного числа ввели строку (((. Исправьтесь
Введите операцию (+, -, *, / или 0 для выхода):
"""


def my_calc():
    actions = ['+', '-', '*', '/']
    action = input("Введите операцию (+, -, *, / или 0 для выхода): ")
    if action == '0':
        return
    elif action not in actions:
        print("Ошибка! Попробуйте снова.")
        my_calc()
    else:
        one = input("Введите первое число:")
        two = input("Введите второе число:")
        try:
            one = int(one)
            two = int(two)
        except ValueError:
            print('Неправильный ввод.')
            my_calc()
            return
        if action == '+':
            print(f'{one} {action} {two} = {one + two}')
        elif action == '-':
            print(f'{one} {action} {two} = {one - two}')
        elif action == '*':
            print(f'{one} {action} {two} = {one * two}')
        else:
            try:
                print(f'{one} {action} {two} = {one / two}')
            except ZeroDivisionError:
                print('Ошибка. Деление на ноль')
        my_calc()


my_calc()
