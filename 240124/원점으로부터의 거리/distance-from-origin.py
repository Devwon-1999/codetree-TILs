class point:
    def __init__(self, x, y, num):
        self.x = x
        self.y = y
        self.num = num

N = int(input())

points = []

for i in range(N):
    x, y = map(int, input().split())
    points.append(point(x, y, i + 1))

points.sort(key = lambda x : (abs(0-x.x) + abs(0-x.y)))

for i in range(len(points)):
    print(points[i].num)