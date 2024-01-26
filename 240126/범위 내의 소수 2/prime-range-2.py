def isPrime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True


a, b = map(int, input().split())

cnt = 0

for i in range(a, b + 1):
    if isPrime(i):
        cnt += 1

print(cnt)