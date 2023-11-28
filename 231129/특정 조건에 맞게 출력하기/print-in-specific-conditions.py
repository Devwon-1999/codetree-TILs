arr = list(map(int, input().split()))
result = list()
for i in arr:
    if i % 2 == 1:
        i += 3
        result.append(i)
    else:
        i //= 2
        result.append(i)

for i in result:
    if i == 0:
        break
    print(i, end=' ')