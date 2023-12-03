n = int(input())

numList = list(map(int, input().split()))

for i in numList:
    if numList.count(i) >= 2:
        while i in numList:
            numList.remove(i)


if max(numList):
    print(max(numList))
else:
    print(-1)