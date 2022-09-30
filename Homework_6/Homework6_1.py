# Написать функцию перевода десятичного числа в двоичное и обратно, без
# использования функции int
def dec_in_bin(dvoich):
    dvoich = str(bin(dvoich))
    dvoich = dvoich.removeprefix('0b')
    return dvoich


def bin_in_dec(desiatichnoe):
    desiatichnoe = result


result = dec_in_bin(int(input()))
print(result)

