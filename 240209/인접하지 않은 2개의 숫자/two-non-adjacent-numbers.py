n = int(input())

numList = list(map(int, input().split()))
max_val = 0
for i in range(n):
    for j in range(i + 2, n):
            max_val = max(max_val, numList[i] + numList[j])

print(max_val)