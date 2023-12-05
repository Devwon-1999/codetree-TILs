numList = list()
for i in range(4):
    tempList = list(map(int, input().split()))
    numList.append(tempList)

addNum = 0

for i in range(4):
    for j in range(0, i+1):
        addNum += numList[i][j]
print(addNum)