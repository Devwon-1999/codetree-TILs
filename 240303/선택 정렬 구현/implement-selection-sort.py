N = int(input())

numList = list(map(int, input().split()))

for i in range(N - 1):
    min_val = i
    for j in range(i + 1, N):
        if numList[j] < numList[min_val]:
            min_val = j
    temp = numList[i]
    numList[i] = numList[min_val]
    numList[min_val] = temp

for i in numList:
    print(i, end = " ")