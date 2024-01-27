def gcd(a, b):  #최대공약수
    while b:
        a, b = b, a % b
    return a

n = int(input())
numlist = list(map(int, input().split()))
x = int(input())
result = []

for i in numlist:
    if gcd(x, i) == 1:
        result.append(i)

print("%.2f" % (sum(result) / len(result)))
