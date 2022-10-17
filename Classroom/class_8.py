# Реализовать класс CallbackData, принимающий на вход неограниченное количество аргументов в виде строк, а так же
# аргумент prefix (user) в виде строки
# 'target', 'action', 'id'
# Реализовать метод new, принимающий неограниченное количество аргументов, НО количество должно совпадать с количеством
# на вход конструктора 'category', 'all', '0'
# и возвращать user:category:all:0
# Реализовать
from datetime import datetime, timedelta

# data = datetime.now()
# dataplus = []
# delta = timedelta(minutes=30)
# plus = data + timedelta(minutes=30)
# datastr = plus.strftime("%d.%m.%Y %H:%M:%S")
# dataplus.append(datastr)
# print(dataplus)
date_string = "17.10.2022 10:00:00"
start_time = datetime.strptime(date_string, "%d.%m.%Y %H:%M:%S")
timeline = []
graph = 0
delta = timedelta(minutes=30)
while graph < 18:
    start_time += delta
    data_to_str = start_time.strftime("%d.%m.%Y %H:%M:%S")
    timeline.append(data_to_str)
    graph += 1
print(timeline)
