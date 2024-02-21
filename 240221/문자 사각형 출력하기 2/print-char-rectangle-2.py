n = int(input())

alpha = [[0] * n for i in range(n)]
dxs, dys = [0, 0] , [1, -1]

def in_range(x, y):
    return 0 <= x and x < n and 0 <= y and y < n

num = 65
for y in range(n):
    for x in range(n):
        for dx, dy in zip(dxs, dys):
            nx, ny = x + dx, y + dy
            if in_range(nx, ny) and alpha[nx][ny] == 0:
                alpha[x][y] = num
        num += 1
        
for i in alpha:
    for j in i:
        print(chr(j), end = " ")
    print()