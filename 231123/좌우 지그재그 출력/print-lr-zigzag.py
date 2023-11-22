n = int(input())
cnt = 1
minus = -1

for i in range(n):
    for j in range(n):
        if i % 2 == 0:
            print(cnt, end=" ")
            cnt += 1
            
        else:
            print(cnt+n+minus, end=" ")
            minus -= 1
    if i % 2 == 1:
        cnt += n

    print()