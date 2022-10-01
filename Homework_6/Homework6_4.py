# Дан список содержащий в себе различные типы данных, отфильтровать таким
# образом, чтобы остались только строки, использование дополнительного списка
# незаконно
list_with_data = input('Enter your list: ')
list_with_data = list(filter(lambda i: i.isalpha(), list_with_data))
print(list_with_data)