# Вывести первые N чисел кратные M и больше K
counter = int(input('Enter count of numbers: '))
splitter = int(input('Enter splitter: '))
k_number = int(input('Enter minimal number: '))
number = 0
numbers = 0
# for i in range(k_number, k_number*splitter**counter):
#     if not i % splitter and number < counter:
#         print(i)
#         number += 1
while number < counter:
    if numbers > k_number and not numbers % splitter:
        print(numbers)
        numbers += splitter
        number += 1
    else:
        numbers += 1
