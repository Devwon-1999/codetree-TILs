n, m = map(int, input().split())
cnt = 1

for i in range(n):
    if i % 2 == 0:

        for i in range(m):
            print(cnt,end=" ")
            cnt += 1
        cnt += m - 1
    else:

        for i in range(m):
            print(cnt,end=" ")
            cnt -= 1
        cnt += m + 1
    print()