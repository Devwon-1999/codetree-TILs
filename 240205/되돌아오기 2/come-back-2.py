x, y = 0, 0
dxs, dys = [0, 1, 0, -1], [1, 0, -1, 0] #북, 동, 남, 서
dir_num = 0

order = input()
orderList = []
for i in order:
    orderList.append(i)

result = []
time = 0
for i in orderList:
    time += 1
    if i == "L": #좌측 90
        dir_num = (dir_num + 3) % 4
    elif i == "R": #우측 90
        dir_num = (dir_num + 1) % 4
    elif i == "F": # 이동
        x, y = x + dxs[dir_num], y + dys[dir_num]
    if x == 0 and y == 0:
        result.append(time)

if result:
    print(result[0])
else:
    print(-1)