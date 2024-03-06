import math

def count_squares(x, y):
    gcd = math.gcd(x, y)
    
    x //= gcd
    y //= gcd

    lcm = gcd * x * y
    squares_with_diagonal = (x + y - 1) * gcd

    return squares_with_diagonal * lcm // (x * y)

x, y = map(int, input().split())

print(count_squares(x, y))