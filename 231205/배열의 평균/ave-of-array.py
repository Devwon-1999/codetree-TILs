numList = list()
for i in range(2):
    tempList = list(map(int, input().split()))
    numList.append(tempList)

for i in numList:
    sumNum = 0
    for j in range(4):
        sumNum += i[j]
    print("%.1f" % (sumNum/4), end=" ")
print()

for i in range(4):
    index = 0
    sumNum = 0
    for j in range(2):
        sumNum += numList[index][i]
        
        index += 1
    print("%.1f" % (sumNum/2), end=" ")
print()


sumNum = 0
for i in numList:
    for j in i:
        sumNum += j

print("%.1f" % (sumNum/8), end=" ")