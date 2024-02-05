n, m = map(int, input().split())

answer = [[0] * m for i in range(n)]

def in_range(x, y):
    return 0 <= x and x < n and 0 <= y and y < m


dxs, dys = [0, 1, 0, -1], [-1, 0, 1, 0]
x, y = 0, 0          
dir_num = 0           

answer[x][y] = 1
cnt = 2
for i in range(2, n * m + 1):
    nx, ny = x + dxs[dir_num], y + dys[dir_num]
    
    if in_range(nx, ny) and answer[nx][ny] == 0:
        x, y = x + dxs[dir_num], y + dys[dir_num]
    else:
        dir_num = (dir_num + 2) % 4
        x, y = x + dxs[dir_num], y + dys[dir_num]
    answer[x][y] = i


for i in range(n):
    for j in range(m):
        print(answer[i][j], end = ' ')
    print()