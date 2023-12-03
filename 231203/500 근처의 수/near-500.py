numList = list(map(int, input().split()))
overList = list()
lowerList = list()

for i in numList:
    if i > 500:
        overList.append(i)
    elif i < 500:
        lowerList.append(i)

print(max(lowerList), min(overList))