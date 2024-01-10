n = int(input())

for i in range(n // 2 + 1):
    for j in range(i):
        print(" ", end ="")
    
    for j in range(1, i + 2):
        print("*" * j, end = "")
    print()
cnt = n

for i in range(n // 2, 0, -1):
    cnt -= 2
    for j in range(i - 1):
        print(" ", end = "")
    for j in range(cnt):
        print("*", end = "")
    print()