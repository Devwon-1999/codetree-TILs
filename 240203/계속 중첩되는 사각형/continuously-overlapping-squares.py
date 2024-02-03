OFFSET = 100
result = [[0] * 201 for i in range(201)]

n = int(input())

cnt = 0

for i in range(n):
    x1, y1, x2, y2 = map(int, input().split())
    x1 += OFFSET
    x2 += OFFSET
    y1 += OFFSET
    y2 += OFFSET
    if cnt % 2 == 0: #RED
        for i in range(x1, x2):
            for j in range(y1, y2):
                result[i][j] = -1
        
    else: #BLUE
        for i in range(x1, x2):
            for j in range(y1, y2):
                result[i][j] = 1
    cnt += 1

answer = 0
for i in range(201):
    for j in range(201):
        if result[i][j] == 1:
            answer += 1

print(answer)