# Дан словарь, ключ - Название страны, значение - список городов, на вход
# поступает город, необходимо сказать из какой он страны
# def search(city):
dict_with_countries = {
    'Belarus': ('Minsk', 'Brest', 'Mogilev', 'Gomel', 'Vitebsk'),
    'Austria': ('Vena', 'Graz', 'Linz', 'Salzburg', 'Insbruk')
}
first_list = ('Minsk', 'Brest', 'Mogilev', 'Gomel', 'Vitebsk')
# print(dict_with_countries.values())
# if 'Minsk' in first_list:
#     print('go')
# print(dict_with_countries.items())
for countries in dict_with_countries.keys():
    if 'Minsk' in dict_with_countries.values():
        print(dict_with_countries.keys(countries))
