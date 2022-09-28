# **Вывести четные числа от 2 до N по 5 в строку
counter = int(input('Enter last number: '))
len_of_string = 5
first_list = []
result_list = []
for i in range(2, counter + 1):
    if not i % 2:
        first_list.append(i)
for i in first_list:
    result_list.append(i)
    if len(result_list) > 4:
        print(result_list)
        result_list.clear()
print(result_list)
