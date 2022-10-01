# Дан список чисел и на вход поступает число N, необходимо сместить список на
# указанное число, пример: [1,2,3,4,5,6,7] N=3 ответ: [5,6,7,1,2,3,4]
numbers = list(input('Enter your list: '))
list_of_numbers = []
for i in numbers:
    if i.isdigit():
        list_of_numbers.append(i)
number = int(input('Enter your number shift: ')) + 1
result_list = ()
result_list = list_of_numbers[number:] + list_of_numbers[0:number]
print(result_list)
# print(list_of_numbers)