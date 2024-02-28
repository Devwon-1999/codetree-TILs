X, Y = map(int, input().split())
cnt = 0
for i in range(X, Y + 1):
    i = str(i)
    temp = []
    for j in i:
        if j not in temp:
            temp.append(j)
    if len(temp) == 2:
        cnt += 1

print(cnt)