def sieve_of_eratosthenes(limit):
    primes = [True] * (limit + 1)
    primes[0] = primes[1] = False
    for i in range(2, int(limit**0.5) + 1):
        if primes[i]:
            for j in range(i * i, limit + 1, i):
                primes[j] = False
    return [num for num in range(limit + 1) if primes[num]]


def count_prime_powers(a, b):
    limit = int(b**0.5) + 1
    primes = sieve_of_eratosthenes(limit)

    cnt = 0
    for prime in primes:
        power = 2
        current = prime ** power
        while current <= b:
            if current >= a:
                cnt += 1
            power += 1
            current = prime ** power

    return cnt


a, b = map(int, input().split())
result = count_prime_powers(a, b)
print(result)