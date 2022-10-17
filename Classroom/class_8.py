# Реализовать класс CallbackData, принимающий на вход неограниченное количество аргументов в виде строк, а так же
# аргумент prefix (user) в виде строки
# 'target', 'action', 'id'
# Реализовать метод new, принимающий неограниченное количество аргументов, НО количество должно совпадать с количеством
# на вход конструктора 'category', 'all', '0'
# и возвращать user:category:all:0
# Реализовать
from datetime import datetime, timedelta

data = datetime.now()
dataplus = []
delta = timedelta(minutes=30)
plus = data + timedelta(minutes=30)
datastr = plus.strftime("%d.%m.%Y %H:%M:%S")
dataplus.append(datastr)
print(dataplus)
