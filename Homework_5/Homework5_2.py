# Сделать калькулятор: у пользователя
# спрашивается число, потом действие и второе число
number_one = float(input('Enter first number: '))
action = input('Enter action: ')
number_two = float(input('Enter second number: '))
if action == '+':
    print(number_one + number_two)
elif action == '-':
    print(number_one - number_two)
elif action == '*':
    print(number_one * number_two)
elif action == '/':
    print(number_one / number_two)