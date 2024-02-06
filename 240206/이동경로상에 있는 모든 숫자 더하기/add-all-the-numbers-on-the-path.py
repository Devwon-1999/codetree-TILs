# N * N 격자에서 정 가운대 북쪽 시작
# T개의 명령 L, R, F(좌 90, 우 90, 바라보는 방향으로 전진)
# 이동할 때마다 칸의 숫자의 누적합
# 격자를 벗어나는 명령 무시

N, T = map(int, input().split()) #N 격자크기 N * N, T 명령의 개수

x, y = N // 2, N // 2 #시작위치 정가운대
dx, dy = [0, 1, 0, -1], [1, 0, -1, 0]#북 동 남 서
dir_num = 3 #시작 방향 서

#명령
order = input() #T개의 명령 문자열 형식 입력
orderList = []
for i in order:
    orderList.append(i)

#격자
base = []
for i in range(N): 
    tempList = list(map(int, input().split()))
    base.append(tempList)

#격자 유효성 확인
def in_range(x, y):
    return 0 <= x and x < N and 0 <= y and y < N

#결과
result = base[x][y]
for i in order:
    if i == "L": #좌 90
        dir_num = (dir_num + 3) % 4
    elif i == "R": #우 90
        dir_num = (dir_num + 1) % 4
    elif i == "F": # 이동
        nx, ny = x + dx[dir_num], y + dy[dir_num]
        if in_range(nx, ny):
            x, y = x + dx[dir_num], y + dy[dir_num]
            result += base[x][y]
        else:
            continue

print(result)