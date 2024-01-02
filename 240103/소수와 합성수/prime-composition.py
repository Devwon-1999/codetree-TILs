n = int(input())
meaList = []
for i in range(1, n + 1):
        if n % i == 0:
            meaList.append(i)

if len(meaList) == 1:
    print("one")
elif len(meaList) == 2:
    print("prime")
else:
    print("composition")