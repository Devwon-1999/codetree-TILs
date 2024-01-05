def sort(numList, n):
    for i in range(n):
        for j in range(n):
            if numList[i] > numList[j]:
                temp = numList[i]
                numList[i] = numList[j]
                numList[j] = temp
    
    for i in numList:
        print(i, end = " ")



n = int(input())

numList = list(map(int, input().split()))

sort(numList, n)