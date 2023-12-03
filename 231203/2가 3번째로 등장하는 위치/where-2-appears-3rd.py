n = int(input())

numList = list(map(int, input().split()))
cnt = 0
findPlace = 0
resultNum = 2

for i in numList:
    if cnt == 3:
        break
    if i == resultNum:
        cnt += 1
    findPlace += 1

print(findPlace)