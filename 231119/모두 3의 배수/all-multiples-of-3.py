numlist = list()
cnt = 0
for i in range(5):
    n = int(input())
    numlist.append(n)

for i in numlist:
    if i % 3 == 0:
        cnt += 1
    else:
        continue

if cnt == 5:
    print(1)
else:
    print(0)