arr = list(map(int, input().split()))
new = list()
for i in arr:
    if i == 0:
        break
    else:
        new.append(i)

avg = sum(new) / len(new)

print(sum(new), "%.1f" % avg)