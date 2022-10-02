# Дан список чисел, необходимо для каждого элемента посчитать сумму его
# соседей, для крайних чисел одним из соседей является число с противоположной
# стороны списка
first_list = [1, 2, 3, 4, 5, 6, 7]
number = list(map(sum(first_list), first_list))

# while number < len(first_list):
#     print(first_list[number - 1] + first_list[number + 1])
#     number += 1
# else:
#     print(first_list[0] + first_list[-1])
