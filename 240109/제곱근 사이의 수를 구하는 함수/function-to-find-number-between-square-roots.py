def printNum(a, b):
    a = a ** (1 / 2) 
    b = b ** (1 / 2)
    cnt = 0
    a, b = int(a), int(b)

    if a > b:
        for i in range(b, a):
            cnt += 1
    else:
        for i in range(a, b):
            cnt += 1
    
    print(cnt)

a, b = map(float, input().split())

printNum(a, b)