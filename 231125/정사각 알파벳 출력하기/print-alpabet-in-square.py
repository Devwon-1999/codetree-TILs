n = int(input())
a = 65
for _ in range(n):
    for _ in range(n):
        print(chr(a),end="")
        a += 1
    print()