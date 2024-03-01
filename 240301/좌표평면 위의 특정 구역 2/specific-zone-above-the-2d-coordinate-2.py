N = int(input())

point_List = []
for i in range(N):
    x, y = map(int, input().split())
    point_List.append([x, y])

answer = []
for i in range(N):
    temp = point_List.copy()
    temp.remove(point_List[i])

    minx, miny, maxx, maxy = 40001, 40001, 0, 0

    for j in temp:
        minx = min(minx, j[0])
        miny = min(miny, j[1])
        maxx = max(maxx, j[0])
        maxy = max(maxy, j[1])
    
    answer.append((maxx - minx) * (maxy - miny))

print(min(answer))