n = int(input())

for i in range(n, 0, -1):
    for j in range(0, n - i +1):
        print(i, end=" ")
        i += 1
    print()