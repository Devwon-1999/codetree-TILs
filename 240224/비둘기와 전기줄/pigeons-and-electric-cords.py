N = int(input())
base = [0 for i in range(11)]
place = [-1 for i in range(11)]
cnt = 0
for i in range(N):
    a, b = map(int, input().split())
    base[a - 1] += 1
    if place[a - 1] == -1:
        place[a - 1] = b
    elif place[a - 1] == 1:
        if b == 0:
            cnt += 1
            place[a - 1] = 0
    elif place[a - 1] == 0:
        if b == 1:
            cnt += 1
            place[a - 1] = 1

print(cnt)