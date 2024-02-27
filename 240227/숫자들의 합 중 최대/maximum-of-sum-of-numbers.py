X, Y = map(int, input().split())
max_val = 0
for i in range(X, Y + 1):
    temp = 0
    i = str(i)
    for j in i:
        j = int(j)
        temp += j
    max_val = max(max_val, temp)

print(max_val)