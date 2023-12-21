n, k = map(int,input().split())
for i in range(1, n+1):
    if k == 1:
        for j in range(1, n+1):
            print(i, end=" ")
        print()
    elif k == 2:
        if i % 2 == 1:
            for j in range(1, n+1):
                print(j, end=" ")
        elif i % 2 == 0:
            for j in range(n, 0, -1):
                print(j, end=" ")
        print()

    elif k == 3:
        for j in range(n):
            print(i * j, end = " ")
        print()