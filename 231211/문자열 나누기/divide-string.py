n = int(input())

numList = list(input().split())
cnt = 0
numStr = ""

for i in numList:
    numStr += i

for i in numStr:
    print(i,end="")
    cnt += 1
    if cnt % 5 == 0:
        print()