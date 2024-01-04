def sumAbsoluteValue(arr):
    result = 0
    for i in arr:
        if i > 0:
            continue
        else:
            i *= -1
        result += i
    return result

n = int(input())
numList = list(map(int, input().split()))

result = sumAbsoluteValue(numList)

print(result)