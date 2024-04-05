n = int(input())

numList = list(map(int, input().split()))

#Bubble Sort(버블 정렬)
for i in range(n - 1):
    for j in range(n - 1 - i):
        if numList[j] > numList[j + 1]:
            temp = numList[j]
            numList[j] = numList[j + 1]
            numList[j + 1] = temp

for i in numList:
    print(i, end = " ")