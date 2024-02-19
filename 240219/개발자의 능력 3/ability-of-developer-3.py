numList = list(map(int, input().split()))

combination1 = []

def get_diff(i, j, k):
    sum1 = numList[i] + numList[j] + numList[k]
    sum2 = sum(numList) - sum1
    return abs(sum1 - sum2)


min_diff = 99999999999

for i in range(6):
    for j in range(i + 1, 6):
        for k in range(j + 1, 6):
            min_diff = min(min_diff, get_diff(i, j, k))

print(min_diff)