OFFSET = 1000
result = [[0] * 2001 for i in range(2001)]

ax1, ay1, ax2, ay2 = map(int, input().split())
bx1, by1, bx2, by2 = map(int, input().split())

ax1 += OFFSET
ay1 += OFFSET
ax2 += OFFSET
ay2 += OFFSET
bx1 += OFFSET
by1 += OFFSET
bx2 += OFFSET
by2 += OFFSET

# a 사각형
for i in range(ax1, ax2):
    for j in range(ay1, ay2):
        result[i][j] += 1

# b 사각형을 제외한 나머지
for i in range(bx1, bx2):
    for j in range(by1, by2):
        result[i][j] -= 1

# a 사각형과 겹치지 않았던 자리 제거
for i in range(2001):
    for j in range(2001):
        if result[i][j] == -1:
            result[i][j] = 0
            
answer = []

for indexy, i in enumerate(result):
    for indexx, j in enumerate(i):
        if j == 1:
            a = indexx
            b = indexy
            answer.append([a, b])

x1 = 2001
x2 = 0
y1 = 2001
y2 = 0

for i in answer:
    if x2 < i[0]:
        x2 = i[0]
    if x1 > i[0]:
        x1 = i[0]
    if y2 < i[1]:
        y2 = i[1]
    if y1 > i[1]:
        y1 = i[1]
        
print((x2 - x1 + 1) * (y2 - y1 + 1))