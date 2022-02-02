"""
Задание 2.

Ваша программа должна запрашивать пароль
Для этого пароля вам нужно получить хеш, используя алгоритм sha256
Для генерации хеша обязательно нужно использовать криптографическую соль
Обязательно выведите созданный хеш

Далее программа должна запросить пароль повторно и вновь вычислить хеш
Вам нужно проверить, совпадает ли пароль с исходным
Для проверки необходимо сравнить хеши паролей

ПРИМЕР:
Введите пароль: 123
В базе данных хранится строка: 555a3581d37993843efd4eba1921
f1dcaeeafeb855965535d77c55782349444b
Введите пароль еще раз для проверки: 123
Вы ввели правильный пароль

Важно: для хранения хеша и соли воспользуйтесь или файлом (CSV, JSON)
или, если вы уже знаете, как Python взаимодействует с базами данных,
воспользуйтесь базой данный sqlite, postgres и т.д.
п.с. статья на Хабре - python db-api
"""
import hashlib
import uuid
import csv
import os


def hash_password(password):
    salt = uuid.uuid4().hex
    return hashlib.sha256(salt.encode() + password.encode()).hexdigest() + ':' + salt


def check_password(hashed_password, user_password):
    password, salt = hashed_password.split(':')
    return password == hashlib.sha256(salt.encode() + user_password.encode()).hexdigest()


def csv_dict_writer(path_file, fieldnames, out_data):
    with open(path_file, "w", newline='') as out_file:
        writer = csv.DictWriter(out_file, delimiter=';', fieldnames=fieldnames)
        writer.writeheader()
        for row in out_data:
            writer.writerow(row)


def csv_dict_reader(file_obj, user_login):
    reader = csv.DictReader(file_obj, delimiter=';')
    for line in reader:
        if line["username"] == user_login:
            return line["key_salt"]
    # если пользователь не найден
    return 0


if not os.path.exists("dict_output.csv"):
    users = [
        ['Brent', hash_password('mypassword')],
        ["Tyrese", hash_password("Hirthe")],
        ["Jules", hash_password("Dicki")],
        ["Dedric", hash_password("Medhurst")]
    ]
    data = ["username,key_salt".split(",")]
    for user in users:
        data.append([user[0], user[1]])
        my_list = []
        fields = data[0]
        for values in data[1:]:
            inner_dict = dict(zip(fields, values))
            my_list.append(inner_dict)
        path = "dict_output.csv"
        csv_dict_writer(path, fields, my_list)

'''
По умолчанию, логин 'Brent', для того чтобы из файла считать хэш и 'соль' и сравнить с введенным паролем.
Поэтому два раза не запрашиваю пароль
'''
login = 'Brent'
new_pass = input('Введите пароль: ')
hashed_password = hash_password(new_pass)
print('Строка для хранения в базе данных: ' + hashed_password)

with open("dict_output.csv", "r") as file:
    user_hash = csv_dict_reader(file, login)

if check_password(user_hash, new_pass):
    print('Вы ввели правильный пароль')
else:
    print('Извините, но пароли не совпадают')
