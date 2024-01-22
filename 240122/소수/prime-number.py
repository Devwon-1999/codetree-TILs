a, b = map(int, input().split())
result = []

for i in range(a, b + 1):
    temp = []
    for j in range(1, i + 1):
        if i % j == 0:
            temp.append(j)
    if len(temp) == 2:
        result.append(i)
            

print(sum(result))
print(min(result))