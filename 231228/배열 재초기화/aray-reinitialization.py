n = int(input())
numList = []

for i in range(n):
    temp = list(map(int, input().split()))
    numList.append(temp)



for i in range(n):
    for j in range(n):
        if i % 2 == 0:
            numList[i][j] = 1
        if j % 2 == 1: 
            numList[i][j] = 2   
for i in numList:
    for j in i:
        print(j, end = " ")
    print()