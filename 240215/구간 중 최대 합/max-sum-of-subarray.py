n, k = map(int, input().split())
numList = list(map(int, input().split()))
result = []

for i in range(n - k + 1):
    temp = 0
    for j in range(i, i + k):
        temp += numList[j]
    result.append(temp)
print(max(result))