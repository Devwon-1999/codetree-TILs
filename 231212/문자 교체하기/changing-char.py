a, b = input().split()

result = ""

alist = list(a)
blist = list(b)

for i in range(2):
    print(alist[i], end="")

for i in range(2,len(blist)):
    print(blist[i], end="")