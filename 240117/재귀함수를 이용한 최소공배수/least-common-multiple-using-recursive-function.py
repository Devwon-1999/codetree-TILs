def min_multiple(numList):
    base = 1
    for i in numList:
        if base % i != 0:
            return min_multiple(base + 1)
    return base


n = map(int, input().split())

numList = list(map(int, input().split()))

print(min_multiple(numList))