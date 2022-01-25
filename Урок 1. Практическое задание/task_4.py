#-*- coding: utf-8 -*-
"""
Задание 4.

Для этой задачи:
1) придумайте 2-3 решения (обязательно с различной сложностью)
2) оцените сложность каждого решения в нотации О-большое
3) сделайте вывод, какое решение эффективнее и почему

Сама задача:
Пользователи веб-ресурса проходят аутентификацию.
В системе хранятся логин, пароль и отметка об активации учетной записи.

Нужно реализовать проверку, может ли пользователь быть допущен к ресурсу.
При этом его учетка должна быть активирована.
А если нет, то польз-лю нужно предложить ее пройти.

Приложение должно давать ответы на эти вопросы и быть реализовано в виде функции.
Для реализации хранилища можно применить любой подход,
который вы придумаете, например, реализовать словарь.

Примечание: ПРОШУ ВАС ВНИМАТЕЛЬНО ЧИТАТЬ ЗАДАНИЕ!
"""
users = [
    {"login" : "mike", "password": '111', "activeted": True},
    {"login" : "nike", "password": '222', "activeted": False},
    {"login" : "anna", "password": '333', "activeted": True},
    {"login" : "olga", "password": '444', "activeted": False}
    ]


def get_user(user_dict):
    for k, v in user_dict.items():
        if k == "activeted":
            if  not v:
                i = int(input("%s пожалуйста активируйте учетную запись (нажмите 1 - для активации)" % user_dict.get("login")))
                if i  == 1:
                    print("active")
                    user_dict["activeted"] = True
                else:
                    print("Активация не пройдена")
            else:
                print("{}, Ваша учетка активирована".format(user_dict.get("login")))


for user_dict in users:
    get_user(user_dict)

print(users)

