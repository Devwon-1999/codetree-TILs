n = int(input())
base = [[2 for j in range(i + 1)] for i in range(n)]

for i in range(2, n):
    for j in range(1, i):
        base[i][j] = base[i - 1][j - 1] + base[i - 1][j]

for i in base:
    for j in i:
        print(j, end = " ")
    print()