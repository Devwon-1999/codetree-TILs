n = int(input())

numList = list(map(int, input().split()))

for i in numList:
    if numList.count(i) >= 2:
        while i in numList:
            numList.remove(i)


if len(numList) == 0:
    print(-1)
else:
    print(max(numList))