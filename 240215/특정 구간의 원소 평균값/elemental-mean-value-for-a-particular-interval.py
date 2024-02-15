N = int(input())

numList = list(map(int, input().split()))
answer = 0
for i in range(N):
    for j in range(i, N):
        tempList = []
        temp = 0
        cnt = 0
        for k in range(i, j + 1):
            tempList.append(numList[k])
            temp += numList[k]
            cnt += 1
        if temp / cnt in tempList:
            answer += 1

print(answer)