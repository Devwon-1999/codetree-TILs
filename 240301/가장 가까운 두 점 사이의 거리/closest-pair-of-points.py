n = int(input())

pointList = []
for i in range(n):
    x, y = map(int, input().split())
    pointList.append([x, y])

pairPointList = []
for i in range(n):
    for j in range(i + 1, n):
        pairPointList.append([pointList[i],pointList[j]])

answer = []
for a, b in pairPointList:
    value = ((a[0] - b[0]) * (a[0] - b[0])) + ((a[1] - b[1]) * (a[1] - b[1]))
    answer.append(value)

print(min(answer))