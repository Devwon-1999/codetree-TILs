su = list()
for _ in range(10):
    a = int(input())
    if a >= 0 and a <= 200:
        su.append(a)
avg = sum(su)/len(su)


print(sum(su), end=' ')
print("%0.1f" % avg)