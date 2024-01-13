def decimal(n):
    if n < 2:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True


a, b = map(int, input().split())

primeList = []


for i in range(a, b + 1):
    if decimal(i):
        primeList.append(i)

if primeList:
    print(sum(primeList))
else:
    print(0)