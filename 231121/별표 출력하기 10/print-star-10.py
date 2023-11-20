n = int(input())
for i in range(1, n*2+1):
    if i % 2 == 1:
        print("* " * (1 + (i // 2)), end=" ")
        print()
    elif i % 2 == 0:
        print("* " * (n - (i - 1) // 2), end=" ")
        print()