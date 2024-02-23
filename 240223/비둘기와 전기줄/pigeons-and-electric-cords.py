N = int(input())
base = [0 for i in range(11)]
for i in range(N):
    a, b = map(int, input().split())
    base[a - 1] += 1

answer = 0
for i in base:
    cnt = 0
    for j in range(i):
        cnt += 1
    if cnt % 2 == 0:
        answer += cnt / 2

print(int(answer))