x, y = 0, 0
dx = [0, 1, 0, -1]#북 동 남 서
dy = [1, 0, -1, 0]#북 동 남 서
dir_num = 0

temp = input()
order = []
for i in range(len(temp)):
    order.append(temp[i])

for i in order:
    if i == "L": #좌 90
        dir_num = (dir_num + 3) % 4
    elif i == "R": #우 90
        dir_num = (dir_num + 1) % 4
    elif i == "F": # 이동
        x, y = x + dx[dir_num], y + dy[dir_num]

print(x, y)