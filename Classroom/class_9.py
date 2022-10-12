with open('for_class_9.txt', 'r', encoding='utf-8') as file:
    N = 0
    for line in file:
        space_count = line.count(' ')
        if space_count:
            space_count += 1
        print(space_count)
        print(line.strip())
