# Дан список чисел, необходимо для каждого элемента посчитать сумму его
# соседей, для крайних чисел одним из соседей является число с противоположной
# стороны списка
input_list = [1, 2, 3, 4, 5, 6, 7]
for i in range(len(input_list)):
    if i != len(input_list) - 1:
        print(input_list[i-1] + input_list[i+1])
    else:
        print(input_list[i-1] + input_list[0])