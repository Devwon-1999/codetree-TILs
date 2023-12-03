n = int(input())

numList = list(map(int, input().split()))
minusList = list()

for i in range(0, n):
    if i == n-1:
        break
    tempNum = numList[i+1] - numList[i]
    minusList.append(tempNum)

print(min(minusList))