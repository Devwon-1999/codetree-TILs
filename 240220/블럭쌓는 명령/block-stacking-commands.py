N, K = map(int, input().split())
base = [0 for i in range(N + 1)]

for i in range(K):
    x, y = map(int, input().split())
    for i in range(x, y + 1):
        base[i] += 1

base.pop(0)
base = sorted(base)

center = N // 2
print(base[center])