def addNum(n):
    temp = 0
    for i in range(n, 101, 2):
        temp += i

    print(temp)

n = int(input())
addNum(n)