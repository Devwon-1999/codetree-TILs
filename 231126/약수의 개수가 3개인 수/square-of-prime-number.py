start, end = map(int, input().split())
cnt = 0
for i in range(start, end+1):
    add = 0
    for j in range(1, i+1):
        if i % j == 0:
            add += 1
    if add == 3:
        cnt += 1
print(cnt)