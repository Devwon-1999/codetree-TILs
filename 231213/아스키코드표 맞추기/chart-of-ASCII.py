arr = list(map(int, input().split()))
resultList = []
for i in arr:
    temp = chr(i)
    resultList.append(temp)

for i in resultList:
    print(i, end =" ")