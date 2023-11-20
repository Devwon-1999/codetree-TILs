n = int(input())
jump = 1
for i in range(n):
    for j in range(n * 2 - 1):
        print("*", end = " ")
    print()
    n -= 1
    for i in range(jump):
        print(" ", end = " ")
    jump += 1