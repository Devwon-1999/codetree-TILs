def decimal(n):
    isPrime = True
    for i in range(2, n - 1):
        if n % i == 0:
            isPrime = False
            return isPrime
    return True


a, b = map(int, input().split())

primeList = []

if a == 1 and b == 1:
    print(1)
else:
    for i in range(a, b + 1):
        if decimal(i):
            primeList.append(i)

    print(sum(primeList))