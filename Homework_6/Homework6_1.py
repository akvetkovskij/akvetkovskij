# Написать функцию перевода десятичного числа в двоичное и обратно, без
# использования функции int
def dec_in_bin(dvoich):
    dvoich = int(dvoich)
    bin_number = ''
    while dvoich > 0:
        bin_number = str(dvoich % 2) + bin_number
        dvoich = dvoich // 2
    return bin_number


def bin_in_dec(s):
    number = 1
    out = 0
    for i in s[::-1]:
        if i == '1':
            out += number
        number <<= 1
    return out


result = dec_in_bin(input('Enter your number: '))
print(result)
result_2 = bin_in_dec(result)
print(result_2)
