# Пользователь вводит 3 числа, сказать сколько из них положительных
# и сколько отрицательных
first_number = int(input('Enter your first number: '))
second_number = int(input('Enter your second number: '))
third_number = int(input('Enter your third number: '))
comparison_1 = first_number >= 0
comparison_2 = second_number >= 0
comparison_3 = third_number >= 0
positive_number = comparison_1 + comparison_2 + comparison_3
negative_number = 3 - positive_number
print('Quantity of positive numbers is ' + str(positive_number))
print('Quantity of negative numbers is ' + str(negative_number))
