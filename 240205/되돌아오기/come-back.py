N = int(input())

x, y = 0, 0
dxs, dys = [0, 1, -1, 0], [1, 0, 0, -1] #동북남서
dir_num = 0
time = 0
result = 0
for i in range(N):
    direction, distance = input().split()
    distance = int(distance)

    if direction == "E":
        dir_num = 0
    elif direction == "N":
        dir_num = 1
    elif direction == "S":
        dir_num = 2
    elif direction == "W":
        dir_num = 3
        
    for i in range(distance):
        time += 1
        x, y = x + dxs[dir_num], y + dys[dir_num]
        if x == 0 and y == 0:
            result = time
        
if result:
    print(result)
else:
    print(-1)