# ЗАНЯТИЕ 5

# заполнить список четными числами в квадрате от 1 до N
# n = int(input())
# some_list = []
# for i in range(n):
#     if i % 2 == 0:
#         some_list.append(i**2)
# print(some_list)

# Спрашивать у пользователя данные с клавиатуры, пока он не введет число
# input_data = input()
# while not input_data.isdigit():
#     input_data = input()

# В строке определить количество не пересекающихся пар одинаковых символов рядом стоящих: Hello
# text = input()
# number = 0
# for i in range(len(text)-1):
#     if text[i] == text[i+1]:
#         number +=1
# print(number)
# text = input()
# number = 0
# i = 0
# while i < len(text) - 1:
#     if text[i] == text[i+1]:
#         number += 1
#         i += 1
#     i += 1
# print(number)

# Дано целое положительное число N, вывести максимальную степень числа 2, в котором 2 не превышает
# N=34, 2^5=32, 32<=34 ответ 5
# number = int(input())
# n = 0
# while 2**n <= number:
#     n += 1
# print(n-1)

# ЗАНЯТИЕ 6

# Вводится многозначное число, использую map и lambda, сформировать список цифр введенного числа
# чтобы все цифры в получившемся списке были по типу int
# number = input()
# number = list(map(lambda x: int(x), number))
# print(number)

# Вводится текст из нескольких предложений, каждое предложение разбито "."
# сказать сколько слов в каждом предложении
# text = input()
# text = text.split('. ')
# word_count = list(map(lambda x: x.count(' ') + 1, text ))
# print(word_count)

# Вводится строка, содержащая все, что угодно, необходимо просуммировать цифры из этой строки
# text = input()
# numbers = list(filter(lambda x: x.isdigit(), text))
# numbers = list(map(lambda x: int(x), numbers))
# numbers = sum(numbers)
# print(numbers)

# Вводится число, суммировать цифры до тех пор, пока не получится однозначное чосло
# прим: 856 -> 19 -> 1
