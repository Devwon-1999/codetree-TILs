n = int(input())
numList = list(map(int, input().split()))
numList.sort()

cnt = 0
i = 0
j = 1

while j < n:
    if numList[j] >= numList[i] * 0.9:
        cnt += j - i
        j += 1
    else:
        i += 1
        if i == j:
            j += 1

print(cnt)