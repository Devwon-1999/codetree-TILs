def power(base, exponent):
    if exponent == 0:
        return 1
    else:
        return base * power(base, exponent - 1)

base, exponent = map(int, input().split())

result = power(base, exponent)
print(result)