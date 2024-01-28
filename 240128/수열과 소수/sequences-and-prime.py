def isPrime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

n = int(input())
numList = list(map(int, input().split()))
add = 0
for i in numList:
    if isPrime(i):
        add += i

print(add)