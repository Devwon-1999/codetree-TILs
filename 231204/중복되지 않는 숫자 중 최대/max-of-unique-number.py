n = int(input())

numList = list(map(int, input().split()))

maxUnique = -1

numSet = set()

for i in numList:
    if i not in numSet:
        numSet.add(i)
        maxUnique = max(maxUnique,i)

print(maxUnique if maxUnique != -1 else -1)