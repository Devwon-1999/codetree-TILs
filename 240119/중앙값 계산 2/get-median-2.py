n = int(input())

numList = list(map(int, input().split()))
temp = []
for i in range(len(numList)):
    temp.append(numList[i])
    temp.sort()
    if i % 2 == 0:
        if i == 0:
            print(temp[i], end = " ")
        else:
            print(temp[i // 2], end = " ")