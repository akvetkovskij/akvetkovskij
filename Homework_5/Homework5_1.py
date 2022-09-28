# Вывести первые N чисел кратные M и больше K
counter = int(input('Enter count of numbers: '))
splitter = int(input('Enter splitter: '))
k_number = int(input('Enter minimal number: '))
number = 0
for i in range(k_number, 1000000):
    if not i % splitter and number < counter:
        print(i)
        number += 1
