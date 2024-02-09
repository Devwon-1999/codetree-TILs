n = int(input())
numList = list(map(int, input().split()))
cnt = 0
numList.sort()
for i in range(n):
    for j in range(i + 1, n):
        if min(numList[i],numList[j]) >= max(numList[i],numList[j]) * 0.9:
            cnt += 1
print(cnt)