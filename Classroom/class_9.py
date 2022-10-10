with open('for_class_9.txt', 'r', encoding='utf-8') as file:
    N = 0
    for i in file:
        i.strip()
            N += 1
print(N)