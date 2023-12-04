n = int(input())

numList = list(map(int,input().split()))
resultList = list()

for i in range(n):
        if numList.count(i) >= 2:
            while i in numList:
                numList.remove(i)
        else:
            continue

if len(numList) >= 1:
    print(max(numList))
else:
    print(-1)