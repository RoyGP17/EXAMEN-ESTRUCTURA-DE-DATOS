def decimal_a_hexadecimal(decimal):
    if decimal == 0:
        return 0
    else:
        digitos = '0123456789ABCDEF'
        return decimal_a_hexadecimal(decimal // 16) + digitos[decimal % 16]

print(decimal_a_hexadecimal(8642))