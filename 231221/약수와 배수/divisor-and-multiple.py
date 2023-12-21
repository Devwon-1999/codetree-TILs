n = int(input())

numList = list(map(int, input().split()))
baeList = list()
yakList = list()
k = int(input())

for i in numList:
    if k % i == 0:
        yakList.append(i)

    elif i % k == 0:
        baeList.append(i)

if k not in yakList:
    yakList.append(k)
if k not in baeList:
    baeList.append(k)

print(sum(yakList))
print(sum(baeList))