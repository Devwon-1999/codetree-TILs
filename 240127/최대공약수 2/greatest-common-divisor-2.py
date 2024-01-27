def gcd(a, b):  #최대공약수
    while b:
        a, b = b, a % b
    return a


def combinations(arr):
    result = []
    for i in range(len(arr)):
        for j in arr[i + 1:]:
            result.append((arr[i], j))
    return result

N = int(input())
numList = list(map(int, input().split()))
base = combinations(numList)
result = []

for i in base:
    result.append(gcd(i[0],i[1]))

print(sum(result))