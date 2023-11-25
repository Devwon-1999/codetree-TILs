n = int(input())
a = 65
for i in range(n):
    print("  " * i,end="")
    for _ in range(n, 0, -1):
        print(chr(a),end=" ")
        a += 1
        
        if a == 91:
            a = 65
    print()
    n -= 1