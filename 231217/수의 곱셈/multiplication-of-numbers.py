a, b, c = map(int, input().split())

casesList = [a*b, b*c, c*a, a*b*c]
resultList = []
secondList = []
for i in casesList:
    if i % 2 == 1:
        resultList.append(i)
    else:
        secondList.append(i)

if resultList:
    print(max(resultList))
else:
    print(max(secondList))