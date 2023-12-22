n = int(input())

for i in range(n):
    a, b, order = input().split()
    a = int(a)
    b = int(b)
    if order == "s":
        print(a * b)
    elif order == "t":
        print("%.1f" % (a * b / 2))
    else:
        continue