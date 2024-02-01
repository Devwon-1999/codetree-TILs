def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def count_primes(a, b):
    return sum(1 for num in range(a, b + 1) if is_prime(num))

a, b = map(int, input().split())
result = count_primes(a, b)
print(result)