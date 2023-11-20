n = int(input())

for i in range(n):
    for _ in range(n):
        print("*",end='')
    for _ in range(1, i+1):
        print(" "*2, end='')    
    for _ in range(n):
        print("*",end='')
    print()
    n -= 1