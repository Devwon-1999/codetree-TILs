N, K = map(int, input().split())
base = [0 for i in range(101)]

for i in range(N):
    candy, index = map(int, input().split())
    base[index - 1] = candy
result = []
for i in range(K, 100 - K):
    candy_cnt = 0
    for j in range(i - K, i + K + 1):
        candy_cnt += base[j]
    result.append(candy_cnt)

print(max(result))