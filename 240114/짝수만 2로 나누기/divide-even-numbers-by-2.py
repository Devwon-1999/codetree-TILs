def modify(numList):
    for i in range(N):
        if numList[i] % 2 == 0:
            numList[i] //= 2



N = int(input())
numList = list(map(int, input().split()))

modify(numList)

for i in numList:
    print(i, end = " ")