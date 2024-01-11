num = input()

integer, decimal = map(str, num.split('.'))

binaryinteger = bin(int(integer))[2:]

binarydecimal = ''
decimal = '0.' + decimal
decimal = float(decimal)

decimal_places = 6 
for _ in range(decimal_places):
    decimal *= 2
    binarydecimal += str(int(decimal))
    decimal -= int(decimal)

result = f"{binaryinteger}.{binarydecimal[:4]}"

print(result)