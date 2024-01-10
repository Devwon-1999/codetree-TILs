n = int(input())
cnt = n
start = 1
for i in range(n // 2 + 1):
    for j in range(i):
        print(" ", end ="")
    
    for j in range(start):
        print("*" , end = "")
    print()
    start += 2
cnt = n

for i in range(n // 2, 0, -1):
    cnt -= 2
    for j in range(i - 1):
        print(" ", end = "")
    for j in range(cnt):
        print("*", end = "")
    print()