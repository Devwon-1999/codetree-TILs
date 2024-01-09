n = int(input())

for i in range(n):
    for j in range((n * n) - ((n - i) * (n - i))):
        print(" ", end = "")
    for j in range((n - i) * (n - i)):
        print("*", end = "")
    print()