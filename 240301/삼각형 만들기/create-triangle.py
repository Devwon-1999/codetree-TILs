N = int(input())

points = []
for i in range(N):
    x, y = map(int, input().split())
    points.append([x, y])

print(points)