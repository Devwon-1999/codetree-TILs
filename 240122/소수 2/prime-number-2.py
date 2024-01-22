n = int(input())
result = []

for i in range(2, n + 1):
    temp = []
    for j in range(1, i + 1):
        if i % j == 0:
            temp.append(j)
    if len(temp) == 2:
        result.append(i)


print(len(result))