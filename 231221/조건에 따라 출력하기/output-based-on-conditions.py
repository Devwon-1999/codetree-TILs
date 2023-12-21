n = int(input())

for i in range(n):
    temp = int(input())
    if temp == 0:
            break
    if temp % 3 == 0:
        print(temp // 3)

    else:
        print(temp + 2)