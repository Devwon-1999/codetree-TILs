n, m = map(int, input().split())
S = []

for i in range(n):
    temp = input()
    S.append(temp)

cnt = 0

for j in range(m):
    check = input()

    if check in S:
        cnt += 1

print(cnt)