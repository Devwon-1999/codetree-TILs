N, S = map(int, input().split())
numList = list(map(int, input().split()))

allList = []

# 2개의 원소를 제외한 모든 조합 생성
for i in range(len(numList)):
    for j in range(i+1, len(numList)):
        combination = [numList[k] for k in range(len(numList)) if k != i and k != j]
        allList.append(combination)

sumList = []
for i in allList:
	sumList.append(sum(i))

subList = []
for i in sumList:
	subList.append(abs(i - S))

print(min(subList))