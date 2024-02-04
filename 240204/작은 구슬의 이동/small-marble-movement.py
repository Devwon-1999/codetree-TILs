n, t = map(int, input().split()) # 격자 크기 n 움직이는 시간 t
r, c, d = input().split() #최초 좌표 (r, c) 방향 d
x, y = int(r) - 1, int(c) - 1 # 좌표의 정수화 r 행, c 열


dxs, dys = [0, 1, -1, 0], [1, 0, 0, -1]
mapper = { 'R': 0, 'D': 1, 'U': 2, 'L': 3 }

move_dir = mapper[d] #입력된 방향의 인덱스 대입
def in_range(x, y): # 격자 값 확인
    return 0 <= x and x < n and 0 <= y and y < n

for i in range(t):
    nx, ny = x + dxs[move_dir], y + dys[move_dir]
    if in_range(nx, ny):
        x, y = nx, ny
    else:
        move_dir = 3 - move_dir
    

print(x + 1, y + 1)