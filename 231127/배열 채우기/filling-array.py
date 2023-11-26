arr = list(map(int, input().split()))
new = list()
for i in arr:
    if i == 0:
        break
    else:
        new.append(i)
new.reverse()
for i in new:
    print(i, end=" ")