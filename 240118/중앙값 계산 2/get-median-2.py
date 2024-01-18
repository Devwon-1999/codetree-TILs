n = int(input())

numList = list(map(int, input().split()))
temp = []
for i in range(len(numList)):
    temp.append(numList[i])
    if i % 2 == 0:
        if i == 0:
            print(temp[i], end = " ")
        else:
            print(temp[len(temp) // 2], end = " ")