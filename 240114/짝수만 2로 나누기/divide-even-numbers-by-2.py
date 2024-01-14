def modify(numList):
    for i in numList:
        if i % 2 == 0:
            index = numList.index(i)
            numList[index] = i // 2



N = int(input())
numList = list(map(int, input().split()))

modify(numList)

for i in numList:
    print(i, end = " ")