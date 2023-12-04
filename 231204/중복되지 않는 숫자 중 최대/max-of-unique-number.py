n = int(input())

numList = list(map(int,input().split()))
resultList = list()

for i in range(0, n):
        if numList.count(i) >= 2:
            while i in numList:
                numList.remove(i)
            continue
        else:
            resultList.append(i)

if len(resultList) >= 1:
    print(max(resultList))
else:
    print(-1)