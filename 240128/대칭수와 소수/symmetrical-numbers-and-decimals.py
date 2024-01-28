def isPrime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True


def palindromic(n):
    n = str(n)
    rev_n = "".join(reversed(n))
    if n == rev_n:
        return True
    else:
        return False

n = int(input())

for i in range(n, 1000000000000000000000000):
    if isPrime(i) and palindromic(i):
        print(i)
        break
    else:
        continue