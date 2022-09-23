# Пользователь вводит предложение, заменить все пробелы на "-" 2-мя
# способами
text = input('Enter your first text: ')
text = text.replace(' ', ' - ')
print(text)
text2 = input('Enter your second text: ')
text2 = text2.split()
text2 = ' - '.join(text2)
print(text2)
