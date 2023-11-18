n = int(input())

while True:
    for i in range(n):
        for _ in range(n):
            print("*", end="")
        print("",end=" ")
    print()
    n -= 1
    if n == 0:
        break