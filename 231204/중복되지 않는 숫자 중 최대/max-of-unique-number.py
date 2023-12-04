n = int(input())

numList = list(map(int,input().split()))
resultList = list()

for i in range(n):
        if numList.count(i) >= 2:
            while i in numList:
                numList.remove(i)
        else:
            resultList.append(i)

if len(numList) >= 1:
    print(max(resultList))
else:
    print(-1)