n = int(input())
result = []
if n == 2:
    a, b = map(int, input().split())
    if a > b:
        for i in range(1, b+1):
            if a % i == 0 and b % i == 0:
                result.append(i)

    elif a < b:
        for i in range(1, a+1):
            if a % i == 0 and b % i == 0:
                result.append(i)

    else:
        result.append(a)

elif n == 3:
    numList = list(map(int, input().split()))
    for i in range(1, min(numList) + 1):
        if numList[0] % i == 0 and numList[1] % i == 0 and numList[2] % i == 0:
            result.append(i)
for i in result:
    print(i)