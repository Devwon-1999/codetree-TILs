N = int(input())

base = [[0] * 10001 for i in range(10001)]

OFFSET = 5000

for i in range(N):
    x1, y1, x2, y2 = map(int, input().split())
    x1 += OFFSET
    y1 += OFFSET
    x2 += OFFSET
    y2 += OFFSET
    for i in range(y2, y1):
        for j in range(x1, x2):
            base[i][j] = 1
cnt = 0

for i in base:
    for j in i:
        if j >= 1:
            cnt += 1
print(cnt)