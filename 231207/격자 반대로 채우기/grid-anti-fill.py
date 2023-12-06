n = int(input())

if n % 2 == 0:
    for i in range(n):
        for j in range(n):
            if j % 2 == 0:
                print((n - j - 1) * n + i + 1, end=' ')
            else:
                print((n - j - 1) * n + n - i, end=' ')
        print()
else:
    for i in range(n):
        for j in range(n):
            if j % 2 == 0:
                print((n - j - 1) * n + n - i, end=' ')
            else:
                print((n - j - 1) * n + i + 1, end=' ')
        print()