def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def lcm(a, b):
    return a * b // gcd(a, b)

def list_lcm(numList):
    if len(numList) == 1:
        return numList[0]
    else:
        return lcm(numList[0], list_lcm(numList[1:]))

n = int(input())
numList = list(map(int, input().split()))

result = list_lcm(numList)
print(result)