n, m = map(int, input().split())
nList = list(map(int, input().split()))
mList = list(map(int, input().split()))

resultList = nList + mList

resultList.sort()

for i in resultList:
    print(i, end = " ")