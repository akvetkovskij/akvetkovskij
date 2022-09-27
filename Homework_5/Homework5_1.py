# Вывести первые N чисел кратные M и больше K
counter = int(input('counter'))
splitter = int(input('splitter'))
k_number = int(input('K number'))
number = 0
for i in range(k_number, k_number*splitter):
    if not i % splitter and number < counter:
        print(i)
        number += 1
