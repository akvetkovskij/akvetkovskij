# Дан словарь словарей, ключ внешнего словаря - id пользователя, значение -
# словарь с данными о пользователе (имя, фамилия, телефон, почта), вывести
# имена тех, у кого не указана почта (нет ключа email или значение этого ключа -
# пустая строка)
users_dikt = {
    'user_1': {
        'name': 'Vasya',
        'last name': 'Petrov',
        'phone': '+1234567',
        'email': 'vasya_petrov@gmail.com'
    },
    'user_2': {
            'name': 'Petia',
            'last name': 'Vasilyev',
            'phone': '+456789'
    },
    'user_3': {
            'name': 'Ivan',
            'last name': 'Ivanov',
            'phone': '+5678943',
            'email': 'ivanovivan@gmail,com'
    },
    'user_4': {
            'name': 'Artem',
            'last name': 'Artemiev',
            'phone': '+67964196834',
            'email': ''
    }
}
# for i in users_dikt.keys():
#     for j in users_dikt.keys(i):
#         if users_dikt.get(i)(j) is None:
#             print(users_dikt.get(i)[j]['name'])
# print(users_dikt['user_1']['name'])
# temperary_dict = {}


# def second_dict():
#     for i in users_dikt.items():
#         yield i
#
#
# def theard_dict():
#     yield from second_dict()
#
#
# for i in theard_dict():
#     print(i)
for i in users_dikt.values():
    if not i.get('email'):
        print(i['name'])
