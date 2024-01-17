def sum_of_digit(n):
    if n < 10: 
        return n % 10
    return sum_of_digit(n // 10) + n % 10


def mul(a, b, c):
    return a * b * c


a, b, c = map(int, input().split())

print(sum_of_digit(mul(a, b, c)))