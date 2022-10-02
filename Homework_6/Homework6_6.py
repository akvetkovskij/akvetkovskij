# Дан список рандомных чисел, необходимо отсортировать его в виде, сначала
# четные, потом нечётные
first_list = list(input('Enter your list: '))
second_list = []
result_list = []
result_list = list(filter(lambda i: not int(i) % 2, first_list))
result_list += list(filter(lambda i: int(i) % 2, first_list))
print(result_list)
