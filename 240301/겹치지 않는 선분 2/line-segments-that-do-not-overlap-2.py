N = int(input())
OFFSET = 1000000

base = [0 for i in range(2000001)]
for i in range(N):
    x1, x2 = map(int, input().split())
    x1 += OFFSET
    x2 += OFFSET
    for j in range(x1, x2):
        base[j] += 1

cnt = 0
for i in base:
    if i == 1:
        cnt += 1
print(cnt)