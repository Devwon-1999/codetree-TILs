N, M = map(int, input().split())
dxs, dys = [1, 0, -1, 0], [0, -1, 0, 1]
base = [[0] * N for _ in range(N)]
result = []

def in_range(x, y): # 좌표가 범위 내에 있는지 확인하는 함수
    return 0 <= x and x < N and 0 <= y and y < N


for i in range(M):
    x, y = map(int, input().split())
    x = x - 1
    y = y - 1
    base[x][y] += 1
    cnt = 0
    for dx, dy in zip(dxs, dys): #좌표기준 동서남북의 좌표에 대해서
        nx, ny = x + dx, y + dy
        if in_range(nx, ny) and base[nx][ny] == 1: #좌표 값이 1인경우를 확인 후
            cnt += 1
    if cnt == 3: # 좌표값이 1인 경우가 3번 이상이라면
        print(1)
    else:
        print(0)