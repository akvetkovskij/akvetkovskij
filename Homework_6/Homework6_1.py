# Написать функцию перевода десятичного числа в двоичное и обратно, без
# использования функции int
def dec_in_bin(dvoich):
    dvoich = str(bin(dvoich))
    dvoich = dvoich.removeprefix('0b')
    return dvoich


def bin_in_dec(s):
    number = 1
    out = 0
    for i in s[::-1]:
        if i == '1':
            out += number
        number <<= 1
    return out


result = dec_in_bin(int(input('Enter your number: ')))
print(result)
result_2 = bin_in_dec(result)
print(result_2)