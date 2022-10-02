# Дан список чисел, необходимо его развернуть без использования метода revese и
# функции reversed, а так же дополнительного списка и среза
list_with_data = list(input('Enter your list: '))
number = 0
while number < len(list_with_data)/2:
    list_with_data[number], list_with_data[~number] = list_with_data[~number], list_with_data[number]
    number += 1
print(list_with_data)
# list_with_data.sort()
# list_with_data = list_with_data[::-1]
# print(list_with_data)
