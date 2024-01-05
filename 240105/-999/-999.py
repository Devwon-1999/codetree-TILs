numList = list(map(int, input().split()))

numList.remove(-999)

print(max(numList), min(numList))