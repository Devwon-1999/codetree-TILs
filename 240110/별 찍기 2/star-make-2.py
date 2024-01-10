size, order = map(int, input().split())

if order == 1:
    for i in range(size // 2 + 1):
        for j in range(i + 1):
            print("*", end = "")
        print()

    for i in range(size // 2, 0, -1):
        for j in range(i):
            print("*", end = "")
        print()

elif order == 2:
    for i in range(size // 2 + 1):
        for j in range(size // 2 - i):
            print(" ", end = "")
        for j in range(i + 1):
            print("*", end = "")
        print()

    for i in range(size // 2, 0, -1):
        for j in range(size // 2 - i + 1):
            print(" ", end = "")
        for j in range(i):
            print("*", end = "")
        print()

elif order == 3:
    num = size
    for i in range(size // 2 + 1):
        for j in range(i):
            print(" ", end = "")
        for j in range(num):
            print("*", end = "")
        num -= 2
        print()

    num = 1
    for i in range(size // 2, 0, -1):
        num += 2
        for j in range(i - 1):
            print(" ", end = "")
        for j in range(num):
            print("*", end = "")
        print()


elif order == 4:
    cnt = 0
    for i in range((size // 2) + 1, 0, -1):
        cnt += 1
        for j in range(((size // 2) + 1) - i):
            print(" ", end = "")
        for j in range(i):
            print("*", end = "")
        print()

    for i in range(size // 2):
        for j in range(cnt - 1):
            print(" ", end = "")
        for j in range(i + 2):
            print("*", end = "")
        print()