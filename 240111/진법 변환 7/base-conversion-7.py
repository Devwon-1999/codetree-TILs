input_number = "32.1238"

integer_part, decimal_part = map(str, input_number.split('.'))

binary_integer_part = bin(int(integer_part))[2:]

binary_decimal_part = ''
decimal_part = '0.' + decimal_part
decimal_part = float(decimal_part)

decimal_places = 6 
for _ in range(decimal_places):
    decimal_part *= 2
    binary_decimal_part += str(int(decimal_part))
    decimal_part -= int(decimal_part)

result = f"{binary_integer_part}.{binary_decimal_part[:4]}"

print(result)