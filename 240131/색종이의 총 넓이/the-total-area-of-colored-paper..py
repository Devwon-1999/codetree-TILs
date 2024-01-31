OFFSET = 100

n = int(input())

result = [[0] * 1000 for i in range(1000)]

for i in range(n):
    x1, y1 = map(int, input().split())
    x1 += OFFSET
    y1 += OFFSET
    x2 = x1 + 8
    y2 = y1 + 8
    for i in range(x1, x2):
        for j in range(y1, y2):
            result[i][j] += 1

cnt = 0
for i in result:
    for j in i:
        if j > 0:
            cnt += 1
    
print(cnt)