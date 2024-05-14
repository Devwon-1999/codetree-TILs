n=int(input())
numList=list(map(int, input().split()))

answer=0

for k in range(1, 101):
    cnt=0
    for i in range(n):
        for j in range(i + 1, n): 
            if (numList[i] + numList[j]) / 2 == k:
                cnt+=1
    answer = max(answer, cnt)
print(answer)