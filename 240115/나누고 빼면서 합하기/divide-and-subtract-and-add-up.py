def func(numList, m):
    result = 0
    while m >= 1:
        result += numList[m - 1]
        if m % 2 == 1:
            m -= 1
        else:
            m //= 2

    return result


n, m = map(int, input().split())
numList = list(map(int, input().split()))

result = func(numList, m)

print(result)