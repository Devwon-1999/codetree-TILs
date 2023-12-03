a, b = map(int, input().split())

alist = list(map(int, input().split()))
blist = list(map(int, input().split()))

for i in range(a):
    boolean = True
    for j in range(b):
        if i + j >= a:
            boolean = False
            break
        if alist[i+j] != blist[j]:
            boolean = False
            break
    if boolean:
        print("Yes")
        break
if boolean == False:
    print("No")