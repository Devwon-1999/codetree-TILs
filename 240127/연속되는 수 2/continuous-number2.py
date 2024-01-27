n = int(input())
base = []
for i in range(n):
    temp = int(input())
    base.append(temp)

cnt = 0
for i in range(n):
    if i == 0 or base[i] != base[i - 1]:
        cnt += 1

print(cnt)