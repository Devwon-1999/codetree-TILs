N, K = map(int, input().split())
base = []
for i in range(N):
    temp = int(input())
    base.append(temp)
answer = -1

for i in range(N - K):
    for j in range(i + 1, i + K + 1):
        if base[i] == base[j]:
            answer = base[i]
if N == K:
    for i in range(N):
        cnt = 0
        for j in base:
            if i == j:
                cnt += 1
        if cnt == 2:
            answer = max(answer, i)
print(answer)