def prime_check(num):
    for i in range(2, num):
        if num % i == 0:
            return False
    return True


def digit_sum_even(num):
    digit_num = (num // 10) + (num % 10)
    if digit_num % 2 == 0:
        return True
    else:
        return False


a, b = map(int, input().split())
cnt = 0

for i in range(a, b + 1):
    if prime_check(i) and digit_sum_even(i):
        cnt += 1
    
print(cnt)