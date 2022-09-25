# Без использования collections, написать программу, которая будет
# создавать словарь для подсчитывания количества вхождений каждой
# буквы в текст введенный с клавиатуры
text = input('Enter your text: ')
text_before_list = set(list(text))
second_dict = dict.fromkeys(text_before_list, 0)
for text_before_list in text:
    second_dict[text_before_list] += 1
print(second_dict)




# I dont know how to use this:

# text = 'hello'
# data = {i: i for i in text}
# print(data)
#
# numbers = [i for i in range(1, 100, 2)]
# print(numbers)