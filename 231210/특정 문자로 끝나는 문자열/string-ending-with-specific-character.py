strList = []
resultList = []
for i in range(10):
    temp = input()
    strList.append(temp)

for i in strList:
    if i[-1] == "e":
        resultList.append(i)

if len(resultList) < 1:
    print("None")
else:
    for i in resultList:
        print(i)