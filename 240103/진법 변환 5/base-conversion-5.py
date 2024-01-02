n, order = map(int, input().split())

if order == 2:
    n = bin(n)

elif order == 8:
    n = oct(n)

elif order == 16:
    n = hex(n)

print(n[2:])