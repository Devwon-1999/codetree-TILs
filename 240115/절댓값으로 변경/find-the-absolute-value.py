def absoloute_value(numlist):
    for i in range(N):
        if numlist[i] < 0:
            numlist[i] *= -1
    

N = int(input())
numList = list(map(int, input().split()))

absoloute_value(numList)

for i in numList:
    print(i, end = " ")