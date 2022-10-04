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
