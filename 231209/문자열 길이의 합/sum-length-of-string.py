n = int(input())

sumLen = 0
cntA = 0

strList = []

for i in range(n):
    tempStr = input()
    strList.append(tempStr)

for i in strList:
    sumLen += len(i)
    
    if i[0] == "a":
        cntA += 1

print(sumLen, cntA)