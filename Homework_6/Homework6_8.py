# Дан словарь, ключ - Название страны, значение - список городов, на вход
# поступает город, необходимо сказать из какой он страны
def search(city):
    dict_with_countries = {
        'Belarus': ('Minsk', 'Brest', 'Mogilev', 'Gomel', 'Vitebsk'),
        'Austria': ('Vena', 'Graz', 'Linz', 'Salzburg', 'Insbruk'),
        'USA': ('New York', 'Chicago', 'Houston', 'Phoenix', 'Columbus'),
        'England': ('London', 'Birmingham', 'Leeds', 'Liverpool', 'Newcastle')
    }
    for i in dict_with_countries.keys():
        if city in dict_with_countries.get(i):
            return i


result = search(input('Enter your city: '))
print(f'Your city in {result}')
