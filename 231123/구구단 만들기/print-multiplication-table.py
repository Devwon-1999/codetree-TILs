a, b = map(int, input().split())

for i in range(1, 10):
    for j in range(b, a-1, -2):
        print(f"{j} * {i} = {i * j}", end="")
        
        if j < b+1 and j > a:
            print(" /",end=" ")

    print()