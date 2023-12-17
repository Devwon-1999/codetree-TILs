a, b, c = map(int, input().split())
tempList = [a, b, c]

mid = 0
tempList.remove(max(tempList))
tempList.remove(min(tempList))

mid = tempList[0]
tempList = [a, b, c]

for i in range(min(tempList), max(tempList)+1):
    for j in range(1, 10):
        if i == mid:
            continue
        print(f"{i} * {j} = {i * j}")