a, b = map(int, input().split())

for i in range(3 * (a - b)):
    for j in range(1, 10):
        print(f"{a} * {j} = {a * j}", end=" ")
        if j % 3 == 0:
            print()
    print()