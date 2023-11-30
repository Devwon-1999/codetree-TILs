inputNum = list(map(int, input().split()))
resultList = list(0 for _ in range(len(inputNum)+1))
answerList = list(0 for _ in range(9))
index = 1

for i in inputNum:
    tenNum = (i % 100) // 10
    resultList.append(tenNum)

for i in resultList:
    if i != 0:
        answerList[i - 1] += 1

for i in answerList:
    print(f"{index} - {i}")
    index += 1