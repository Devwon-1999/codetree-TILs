n = int(input())
meaList = []
for i in range(1, n + 1):
    for j in range(1, n + 1):
        if i % j == 0:
            meaList.append(j)

if len(meaList) == 1:
    print("one")
elif len(meaList) == 2:
    print("prime")
else:
    print("composition")