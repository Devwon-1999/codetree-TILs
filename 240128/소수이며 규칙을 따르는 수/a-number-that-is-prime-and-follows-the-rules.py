def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def digit_square_sum(number):
    return sum(int(digit)**2 for digit in str(number))

def find_special_primes(limit):
    special_primes = []
    for n in range(2, limit + 1):
        current = n
        while current != 1 and current != 4:  # 조건을 만족하면서 1이 되는지 확인
            current = digit_square_sum(current)
        if current == 1 and is_prime(n):
            special_primes.append(n)
    return special_primes

# 입력 받기
limit = int(input())

# 결과 출력
result = find_special_primes(limit)
for prime in result:
    print(prime)