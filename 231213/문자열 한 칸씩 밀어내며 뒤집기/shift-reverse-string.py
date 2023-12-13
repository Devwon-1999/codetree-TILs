s, q = input().split()
q = int(q)

for i in range(q):
    req = int(input())
    if req == 1:
        s = s[1:] + s[0]
        print(s)
    elif req == 2:
        s = s[-1] + s[0:len(s)-1]
        print(s)
    elif req == 3:
        slist = list(s)
        slist.reverse()
        s = ''.join(slist)
        print(s)