def maxValue(a,b,c):
    tempList = [a, b, c]

    return max(tempList)


a,b,c = map(int,input().split())
maxValue = maxValue(a, b, c)

print(maxValue)