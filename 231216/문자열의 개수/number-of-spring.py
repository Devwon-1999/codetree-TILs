cnt = 0
resultList = []
while True:
    temp = input()
    if temp == "0":
        break
    else:
        cnt += 1
        resultList.append(temp)

print(cnt)
for i in range(len(resultList)):
    if i % 2 == 0:
        print(resultList[i])