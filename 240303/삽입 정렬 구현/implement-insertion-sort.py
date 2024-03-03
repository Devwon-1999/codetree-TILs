N = int(input())

numList = list(map(int, input().split()))

for i in range(1, N):
    j = i - 1
    key = numList[i]
    while j >= 0 and numList[j] > key:
        numList[j + 1] = numList[j]
        j -= 1
    numList[j + 1] = key

for i in numList:
    print(i, end = " ")