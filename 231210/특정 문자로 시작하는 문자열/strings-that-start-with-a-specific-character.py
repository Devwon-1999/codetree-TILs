strList = []
resultList = []
addLen = 0
n = int(input())

for i in range(n):
    temp = input()
    strList.append(temp)

firstchar = input()

for i in strList:
    if i[0] == firstchar:
        resultList.append(i)
    
for i in resultList:
    addLen += len(i)


print(f"{len(resultList)} {addLen/len(resultList):.2f}")