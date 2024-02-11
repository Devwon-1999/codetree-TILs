def sieve_of_eratosthenes(n):
    primes = [True] * (n+1)
    primes[0] = primes[1] = False
    for i in range(2, int(n**0.5)+1):
        if primes[i]:
            for j in range(i*i, n+1, i):
                primes[j] = False
    return primes

def count_primes(a, b):
    primes = sieve_of_eratosthenes(b)
    count = sum(1 for i in range(a, b+1) if primes[i])
    return count

a, b = map(int, input().split())
result = count_primes(a, b)
print(result)