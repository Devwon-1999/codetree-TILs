n, t = map(int, input().split())

numList = list(map(int, input().split()))

ans, cnt = 0, 0
if n == 1:
    if numList[0] > t:
        print(1)
    else:
        print(0)
else:
    for i in range(n):
        if i + 1 >= len(numList):
            break
        if i >= 1 and numList[i] > t and numList[i + 1] > t:
            cnt += 1
        else:
            cnt = 1
        ans = max(ans, cnt)

    print(ans)