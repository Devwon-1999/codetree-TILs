def gcd(a, b): #최대공약수
    while b:
        a, b = b, a % b
    return a


n = int(input())
n_list = list(map(int, input().split()))

m = int(input())
m_list = list(map(int, input().split()))

a = 1
for i in n_list:
    a *= i

b = 1
for i in m_list:
    b *= i

print(gcd(a, b) % ((10**9) + 7))