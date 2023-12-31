n = int(input())
cnt = 10
temp = cnt
for i in range(n):
    cnt = temp - (i + 1)
    for j in range(n):
        print(cnt, end=" ")
        if cnt == 1:
            cnt = 1
        else:
            cnt -= 1
    print()