size, order = map(int, input().split())

if order == 1:
    num = 1
    for i in range(1, size + 1):
        if i % 2 == 0:
            for j in range(num + i - 1, num - 1, -1):
                print(j, end=" ")
            num += i
        else:
            for j in range(num, num + i):
                print(j, end=" ")
            num += i
        print()

elif order == 2:
    num = 0
    for i in range(5, 0, -1):
        for j in range(size - i):
            print(" ", end = " ")
        for j in range(i * 2 - 1):
            print(num, end = " ")
        print()
        num += 1

elif order == 3:
    for i in range(1, size):
        for j in range(1, i + 1):
            print(j, end=" ")
        print()

    for i in range(size , 0, -1):
        for j in range(1, i + 1):
            print(j, end=" ")
        print()