n = int(input())
a = 65
for i in range(n):
    for _ in range(i+1):
        print(chr(a),end="")
        a += 1
    print()