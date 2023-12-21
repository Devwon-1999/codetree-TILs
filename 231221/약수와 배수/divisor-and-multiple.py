n = int(input())

numList = list(map(int, input().split()))
baeList = list()
yakList = list()
k = int(input())

for i in range(n):
    if numList[i] % k == 0:
        baeList.append(numList[i])

    if k % numList[i] == 0:
        yakList.append(numList[i])

print(sum(yakList))
print(sum(baeList))