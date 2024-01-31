ax1, ay1, ax2, ay2 = map(int, input().split())
bx1, by1, bx2, by2 = map(int, input().split())
mx1, my1, mx2, my2 = map(int, input().split())

OFFSET = 1000

result = [[0] * 2000 for i in range(2000)]
ax1 += OFFSET
ax2 += OFFSET
ay1 += OFFSET
ay2 += OFFSET
bx1 += OFFSET
bx2 += OFFSET
by1 += OFFSET
by2 += OFFSET
mx1 += OFFSET
mx2 += OFFSET
my1 += OFFSET
my2 += OFFSET
for i in range(ax1, ax2):
    for j in range(ay1, ay2):
        result[i][j] += 1

for i in range(bx1, bx2):
    for j in range(by1, by2):
        result[i][j] += 1

for i in range(mx1, mx2):
    for j in range(my1, my2):
        result[i][j] -= 1
        
cnt = 0
for i in result:
    for j in i:
        if j == 1:
            cnt += 1
    
print(cnt)