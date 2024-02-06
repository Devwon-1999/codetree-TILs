n, m = map(int, input().split())

answer = [[0] * m for i in range(n)]

def in_range(x, y):
    return 0 <= x and x < n and 0 <= y and y < m


dxs, dys = [0, 1, 0, -1], [1, 0, -1, 0]
x, y = 0, 0           
dir_num = 0           
answer[x][y] = 65
cnt = 65
for i in range(2, n * m + 1):
    cnt += 1
    if cnt > 90:
        cnt = 65
    nx, ny = x + dxs[dir_num], y + dys[dir_num]
    
    if not in_range(nx, ny) or answer[nx][ny] != 0:
        dir_num = (dir_num + 1) % 4

    x, y = x + dxs[dir_num], y + dys[dir_num]
    answer[x][y] = cnt


for i in range(n):
    for j in range(m):
        print(chr(answer[i][j]), end = ' ')
    print()