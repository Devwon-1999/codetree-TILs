light, order = map(int, input().split())

lightList = list(map(int, input().split()))

for i in range(order):
    a, b, c = map(int, input().split())

    if a == 1:
        lightList[b-1] = c
    elif a == 2:
        for i in range(b-1, c):
            if lightList[i] == 0:
                lightList[i] = 1
            else:
                lightList[i] = 0
    elif a == 3:
        for i in range(b-1, c):
            lightList[i] = 0
    elif a == 4:
        for i in range(b-1, c):
            lightList[i] = 1

for i in lightList:
    print(i, end=" ")