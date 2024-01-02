n = int(input())
numList = list(map(int, input().split()))

resultList = []
cnt = 0

for i in numList:
    if i % 7 == 0:
        resultList.append(i)
        cnt += 1

print(cnt, sum(resultList), "%.1f" % (sum(resultList) / cnt))