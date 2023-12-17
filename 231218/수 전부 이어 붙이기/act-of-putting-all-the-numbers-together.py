n = int(input())

numList = list(input().split())
numStr = ""
index = 0
for i in numList:
    numStr += i

for value in numStr:
    
    print(value, end="")
    index += 1
    if index == 5:
        print()
        index = 0