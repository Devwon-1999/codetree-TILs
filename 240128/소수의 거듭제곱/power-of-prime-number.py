def isPrime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True


def count_prime_powers(a, b):
    primes = []
    for num in range(a, b + 1):
        if is_prime(num):
            primes.append(num)

    cnt = 0
    for prime in primes:
        power = 2
        while prime ** power <= b:
            cnt += 1
            power += 1

    return cnt


a, b = map(int, input().split())
result = count_prime_powers(a, b)
print(result)