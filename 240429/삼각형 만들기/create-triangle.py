N = int(input())

points = []
for i in range(N):
    x, y = map(int, input().split())
    points.append([x, y])

# print(points)

max_val = 0

for i in range(len(points)):
    for j in range(i + 1, len(points)):
        
        for k in range(j + 1, len(points)):
            cnt = 0
            if points[i][0] - points[j][0] == 0:
                cnt += 1
            if points[j][0] - points[k][0] == 0:
                cnt += 1
            if points[i][0] - points[k][0] == 0:
                cnt += 1
            if points[i][1] - points[j][1] == 0:
                cnt += 1
            if points[j][1] - points[k][1] == 0:
                cnt += 1
            if points[i][1] - points[k][1] == 0:
                cnt += 1

            if cnt == 2:
                a = (points[i][0] * points[j][1]) + (points[j][0] * points[k][1]) + (points[k][0] * points[i][1])
                b = (points[i][1] * points[j][0]) + (points[j][1] * points[k][0]) + (points[k][1] * points[i][0])
                area = abs(a - b)
                max_val = max(max_val, area)

            else:
                continue

            # print(points[i], points[j], points[k])
            # print(cnt)
print(max_val)