n = int(input())

numList = list(map(int, input().split()))
min100 = []
max99 = []
for i in numList:
    if i >= 100:
        min100.append(i)
    else:
        max99.append(i)
if min100:
    if max99:
        if 100 - max(max99) == min(min100) - 100:
            print(max99, end = " ")
        elif 100 - max(max99) > min(min100) - 100:
            print(min(min100), end = " ")
        elif 100 - max(max99) < min(min100) - 100:
            print(max(max99), end = " ")




if not min100:
    print(max(max99), -1, end = " ")
else:
    print(min(min100), end = " ")