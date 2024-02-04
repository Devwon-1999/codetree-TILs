x, y = 0, 0
dx, dy = [1, 0, -1, 0], [0, -1, 0, 1] # 동, 남, 서, 북
N = int(input())

for i in range(N):
    direction, length = input().split()
    length = int(length)

    if direction == "E": # 동
        dir_num = 0
    elif direction == "S": # 남
        dir_num = 1
    elif direction == "W": # 서
        dir_num = 2
    elif direction == "N": # 북
        dir_num = 3
        
    for i in range(length):
        x, y = x + dx[dir_num], y + dy[dir_num]

print(x, y)