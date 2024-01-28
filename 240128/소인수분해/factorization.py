def prime_factors(n):
    factors = []
    i = 2
    while i <= n:
        if n % i == 0:
            factors.append(i)
            n = n / i
        else:
            i = i + 1
    return factors

n = int(input())

if n == 1:
    print(-1)

else:
    result = prime_factors(n)
    for i in result:
        print(i)