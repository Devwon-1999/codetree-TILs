def cul(a, b, c):
    if a % 2 == 0:
        print(a // 2, end = " ")
    else:
        print(a * 3 - 20, end = " ")
    if b % 2 == 0:
        print(b // 2, end = " ")
    else:
        print(b * 3 - 20, end = " ")
    if c % 2 == 0:
        print(c // 2, end = " ")
    else:
        print(c * 3 - 20, end = " ")

a, b, c = map(int, input().split())

cul(a,b,c)