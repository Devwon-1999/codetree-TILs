def lcm(a, b): #최소공배수
    return a * b // gcd(a, b) 


def gcd(a, b): #최대공약수
    while b:
        a, b = b, a % b
    return a


a, b = map(int, input().split())

print(gcd(a, b), lcm(a, b))
