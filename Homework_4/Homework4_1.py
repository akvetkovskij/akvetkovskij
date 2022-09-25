# Заполнить список степенями числа 2 (от 2^1 до 2^n).
inserted_power = int(input('Enter power of 2: '))
power = [2 ** i for i in range(1, inserted_power + 1)]
print(power)
