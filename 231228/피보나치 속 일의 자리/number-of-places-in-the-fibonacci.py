n = int(input())

a, b = map(int, input().split())

numList = []

numList.append(a)
numList.append(b)

index = 2

for i in range(n-2):
    temp = numList[index-2] + numList[index-1]
    if temp > 9:
        temp = temp % 10    
    numList.append(temp)
    index += 1

for i in numList:
    print(i, end = " ")