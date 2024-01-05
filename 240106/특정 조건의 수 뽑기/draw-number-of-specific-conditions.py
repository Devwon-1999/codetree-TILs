n = int(input())

numList = list(map(int, input().split()))
min100 = []
max99 = []
for i in numList:
    if i >= 100:
        min100.append(i)
    else:
        max99.append(i)

if not max99:
    print(-1, end = " ")
else:
    print(max(max99), end = " ")

if not min100:
    print(-1, end = " ")
else:
    print(min(min100), end = " ")