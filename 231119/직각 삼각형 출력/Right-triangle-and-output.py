n = int(input())
for i in range(0, n*2, 2):
    for j in range(i+1):
        print("*",end="")
    print()