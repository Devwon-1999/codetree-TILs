N = int(input())

worktime = []
for i in range(N):
    start, end = map(int, input().split())
    worktime.append([start, end])

fire_1 = []
for i in range(N):
    fire_1.append(worktime[:i] + worktime[i + 1:])

answer = []
for i in fire_1:
    temp = [0 for i in range(1001)]
    for j in i:
        for time in range(j[0], j[1]):
            temp[time] += 1

    cnt = 0
    for i in temp:
        if i != 0:
            cnt += 1
    answer.append(cnt)

print(max(answer))