oneList = list()
twoList = list()

for i in range(3):
    tempList = list(map(int, input().split()))
    oneList.append(tempList)
input()
for i in range(3):
    tempList = list(map(int, input().split()))
    twoList.append(tempList)

for i in range(3):
    for j in range(3):
        print(oneList[i][j] * twoList[i][j], end= " ")
    print()