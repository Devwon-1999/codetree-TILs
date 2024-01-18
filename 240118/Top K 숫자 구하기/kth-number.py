N, K = map(int, input().split())

numList = list(map(int, input().split()))

numList.sort()

print(numList[K - 1])