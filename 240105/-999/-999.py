numList = list(map(int, input().split()))

index999 = numList.index(-999)
numList = numList[0: index999]

print(max(numList), min(numList))