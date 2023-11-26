n = int(input())

arr = list(map(int, input().split()))
result = list()


for i in arr:
    if i % 2 == 0:
        result.append(i)

result.reverse()

for i in result:
    print(i, end=" ")