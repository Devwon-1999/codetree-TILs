n = int(input())
num = 2
for i in range(n):
    for j in range(i):
        print(" ", end = " ")
    for j in range(n - i):
        print(num, end = " ")
        num += 2
        if num > 8:
            num = 2
    print()