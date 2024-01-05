import math

def specialCul(numList):
    indexList = [0, 1, 2]

    maxValueIndex = numList.index(max(numList))
    minValueIndex = numList.index(min(numList))

    numList[maxValueIndex] = math.ceil(numList[maxValueIndex])
    numList[minValueIndex] = math.floor(numList[minValueIndex])

    for i in numList:
        if type(i) == type(0.0):
            midValueIndex = numList.index(i)

    numList[midValueIndex] = round(numList[midValueIndex])

    for i in numList:
        print(i, end = " ")


numList = list(map(float, input().split()))


specialCul(numList)