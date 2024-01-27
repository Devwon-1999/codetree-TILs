def lcm(a, b): #최소공배수
    return a * b // gcd(a, b) 


def gcd(a, b): #최대공약수 
    while b:
        a, b = b, a % b
    return a

N = int(input())
numList = list(map(int, input().split()))

if N == 1:
    print(numList[0], numList[0])

elif N == 2:
    print(gcd(numList[0], numList[1]), lcm(numList[0], numList[1]))

else:
    gcdValue = numList[0]
    lcmValue = numList[0]
    for i in range(1, len(numList)):
        gcdValue = gcd(gcdValue, numList[i])
        lcmValue = lcm(lcmValue, numList[i])
    print(gcdValue, lcmValue)