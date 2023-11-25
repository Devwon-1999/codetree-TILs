n = int(input())
result = list()
for i in range(n):
    add = 0
    a, b = map(int, input().split())
    for j in range(a, b+1):
        if j % 2 == 0:
            add += j
    result.append(add)
for i in result:
    print(i)