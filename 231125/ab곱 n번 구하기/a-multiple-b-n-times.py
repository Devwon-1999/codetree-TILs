n = int(input())
result = list()
for i in range(n):
    mul = 1
    a, b = map(int, input().split())
    for j in range(a, b+1):
        mul *= j
    result.append(mul)
    
for j in result:
    print(j)