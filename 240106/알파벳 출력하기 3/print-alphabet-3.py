n = int(input())
num = 65
for i in range(n, 0, -1):
    for j in range(i):
        print(chr(num), end="")
        num += 1
        if num > 90:
            num = 65
    print()