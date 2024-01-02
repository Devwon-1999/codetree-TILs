size, order = map(int, input().split())
temp = 1
if order == 1:
    for i in range(1, size + 1):
        for j in range(i):
            print("*", end="")
        print()
elif order == 2:
    for i in range(size, 0, -1):
        for j in range(i):
            print("*", end="")
        print()            
elif order == 3:
    for i in range(size - 1, 0, -1):
        for j in range(i):
            print("", end = " ")
        for j in range(temp):
            print("*", end = "")
        temp += 2
        print()