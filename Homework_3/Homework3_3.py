# Пользователь вводит Имя, Возраст и Город, сформировать
# приветственное сообщение путем форматирования 3-мя способами
name = input('Enter your name: ')
city = input('Enter your city: ')
age = input('Enter your age: ')
welcome_text_1 = 'Hellow, ' + name + '! You are from ' + city + '. And you are ' + str(age) + ' years old.'
welcome_text_2 = 'Hellow, {}! You are from {}. And you are {} years old.'.format(name, city, age)
welcome_text_3 = f'Hellow, {name}! You are from {city}. And you are {age} years old.'
welcome_text_4 = 'Hellow, %s! You are from %s. And you are %s years old.' % (name, city, age)
print(welcome_text_1)
print(welcome_text_2)
print(welcome_text_3)
print(welcome_text_4)
