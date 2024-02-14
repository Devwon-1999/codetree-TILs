#입력
N, M = map(int, input().split())
base = []
for i in range(N):
    string = input()

    temp = []
    for j in string:
        temp.append(j)
    base.append(temp)

def in_range(x, y):
    return 0 <= x and x < N and 0 <= y and y < M

dxs, dys = [1, 1, 1, -1, -1, -1, 0, 0], [-1, 0, 1, -1, 0, 1, -1, 1]

cnt = 0
for i in range(N):
    for j in range(M):
        if base[i][j] != "L":
            for dx, dy in zip(dxs, dys):
                curt = 1
                curx = i
                cury = j
                while True:
                    nx = curx + dx
                    ny = cury + dy
                    if in_range(nx, ny) == False:
                        break
                    if base[nx][ny] != "E":
                        break
                    curt += 1
                    curx = nx
                    cury = ny
                
                if curt == 3:
                    cnt += 1
        elif base[i][j] != "E":
            for dx, dy in zip(dxs, dys):
                curt = 1
                curx = i
                cury = j
                while True:
                    nx = curx + dx
                    ny = cury + dy
                    if in_range(nx, ny) == False:
                        break
                    if base[nx][ny] != "E":
                        break
                    else:
                        curt += 1
                        curx = nx
                        cury = ny
                        if base[nx][ny] != "L":
                            break
                        else:
                            curt += 1
                            curx = nx
                            cury = ny
                            
                if curt == 3:
                    cnt += 1
        else: 
            break
print(cnt)