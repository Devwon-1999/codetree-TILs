N, K = map(int, input().split())
base = []
for i in range(N):
    temp = int(input())
    base.append(temp)
answer = -1

for i in range(N - K + 1):
    for j in range(i + 1, i + K + 1):
        if base[i] == base[j - 1]:
            answer = base[i]
        else:
            continue

print(answer)