def sumAbsoluteValue(arr):
    result = 0
    for i in arr:
        if i > 0:
            pass
        else:
            i = -i
        result += i
    return result

n = int(input())
numList = list(map(int, input().split()))

result = sumAbsoluteValue(numList)

print(result)