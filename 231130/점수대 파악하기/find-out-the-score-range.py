scoreList = list(map(int, input().split()))
resultList = [0 for i in range(10)]
score = 100
for i in scoreList:
    if i == 0:
        break
    resultList[(i // 10)-1] += 1
print(resultList)
resultList.reverse()

for i in resultList:
    print(f"{score} - {i}")
    score -= 10