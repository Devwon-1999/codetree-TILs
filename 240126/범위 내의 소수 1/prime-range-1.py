def isPrime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True


a, b = map(int, input().split())
result = []

for i in range(a, b + 1):
    if isPrime(i):
        result.append(i)
if result:
    print(sum(result), min(result))
else:
    print(0, 0)