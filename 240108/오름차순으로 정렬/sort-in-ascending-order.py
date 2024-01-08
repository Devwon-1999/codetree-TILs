n = int(input())

numList = list(map(int, input().split()))

for i in range(len(numList)):
    for j in range(len(numList)):
        if numList[i] < numList[j]:
            temp = numList[i]
            numList[i] = numList[j]
            numList[j] = temp

for i in numList:
    print(i, end = " ")