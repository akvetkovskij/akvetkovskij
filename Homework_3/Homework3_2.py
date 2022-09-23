# Пользователь вводит 3 числа, найти среднее арифмитическое с
# точность 3
first_number = input('Enter your first number: ')
first_number = float(first_number)
second_number = input('Enter your second number: ')
second_number = float(second_number)
third_number = input('Enter your third number: ')
third_number = float(third_number)
average = round((first_number + second_number + third_number)/3, 3)
text_in_print = f'Average of this numbers is {average}'
print(text_in_print)
