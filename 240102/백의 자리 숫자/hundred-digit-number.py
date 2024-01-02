result = [0 for _ in range(10)]

n = int(input())
numList = list(map(int, input().split()))

for i in numList:
    if i // 100 >= 0:
        result[i // 100] += 1
index = 0
for i in result:
    if i != 0:
        print(f"{index} - {i}")
    index += 1