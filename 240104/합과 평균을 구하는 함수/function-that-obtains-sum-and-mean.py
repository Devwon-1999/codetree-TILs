def printSumAvg(a, b, c):
    sumNum = 0
    avgNum = 0
    a = round(a)
    b = round(b)
    c = round(c)

    sumNum = a + b + c
    avgNum = sumNum // 3

    print(sumNum)
    print(avgNum)

a, b, c = map(float, input().split())
printSumAvg(a, b, c)