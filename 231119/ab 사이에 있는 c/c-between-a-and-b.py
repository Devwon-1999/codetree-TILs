a, b, c = map(int, input().split())
numlist = list()
cnt = 0
for i in range(a, b+1):
    numlist.append(i)
    for j in numlist:
        if j % c != 0:
            continue
        elif j % c == 0:
            cnt += 1

if cnt:
    print("YES")
else:
    print("No")