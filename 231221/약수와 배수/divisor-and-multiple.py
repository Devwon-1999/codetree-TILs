n = int(input())

numList = list(map(int, input().split()))
baeList = list()
yakList = list()
k = int(input())

for i in range(n):
    if numList[i] % k == 0:
        yakList.append(k)

    if k % numList[i] == 0:
        baeList.append(k)

print(sum(yakList))
print(sum(baeList))