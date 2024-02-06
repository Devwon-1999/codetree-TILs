N = int(input())

base = [[0] * N for _ in range(N)]

x, y = N - 1, N - 1
dxs, dys = [0, -1, 0, 1], [-1, 0, 1, 0]
dir_num = 0
base[N // 2][N // 2] = 1
base[x][y] = N * N
def in_range(x, y):
    return 0 <= x and x < N and 0 <= y and y < N


for i in range(N * N - 1, 1, -1):
    nx, ny = x + dxs[dir_num], y + dys[dir_num]
    if not in_range(nx, ny) or base[nx][ny] != 0:
        dir_num = (dir_num + 1) % 4
    x, y = x + dxs[dir_num], y + dys[dir_num]
    base[x][y] = i

for i in range(N):
    for j in range(N):
        print(base[i][j], end = ' ')
    print()