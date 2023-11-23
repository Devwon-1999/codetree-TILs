n = int(input())
num = 1
for i in range(n):
    print("  "*(i),end="")
    for j in range(n, 0, -1):
        print(num,end=" ")
        num += 1

        if num >= 10:
            num = 1
    n -= 1
    print()