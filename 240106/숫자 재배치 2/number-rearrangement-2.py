n = int(input())

numList = list(map(int, input().split()))

numList.reverse()

for i in numList:
    print(i, end=" ")