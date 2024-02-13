n = int(input())
numList = list(map(int, input().split()))

result = []

for i in range(n):
    target = 0
    for j in range(n):
        if j != i:
            target += int(numList[j]) * abs(i - j)
    result.append(target)

print(min(result))