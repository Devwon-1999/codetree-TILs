n = int(input())

base = [0 for i in range(n + 2)]

base[0] = 1
base[1] = 1

for i in range(n):
    base[i + 2] = base[i] + base[i + 1]

print(base[n - 1])