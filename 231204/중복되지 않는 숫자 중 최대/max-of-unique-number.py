n = int(input())

numList = list(map(int, input().split()))

maxUnique = -1

for i in range(n):
    isTrue = False

    for j in range(i+1, n):
        if numList[i] == numList[j]:
            isTrue = True
            break

    if not isTrue:
        maxUnique = max(maxUnique,numList[i])

print(maxUnique)