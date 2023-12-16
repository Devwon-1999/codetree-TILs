numList = []
inputList = []
resultList = []
for i in range(1,31):
    numList.append(i)

for i in range(28):
    n = int(input())
    inputList.append(n)

for i in numList:
    if i not in inputList:
        resultList.append(i)

for i in resultList:
    print(i)