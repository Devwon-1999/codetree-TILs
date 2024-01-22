def count_primes(n):
    is_prime = [True] * (n + 1)
    is_prime[0] = is_prime[1] = False

    for i in range(2, int(n**0.5) + 1):
        if is_prime[i]:
            for j in range(i * i, n + 1, i):
                is_prime[j] = False

    primes = [num for num in range(2, n + 1) if is_prime[num]]
    return len(primes)

n = int(input())
result = count_primes(n)
print(result)