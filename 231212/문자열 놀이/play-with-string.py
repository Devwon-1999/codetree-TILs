s, q = input().split()
q = int(q)

for i in range(q):
    n = list(input().split())

    if n[0] == "1":
        lists = list(s)
        n[1] = int(n[1])
        n[2] = int(n[2])
        temp = lists[n[2]-1]
        lists[n[2]-1] = lists[n[1]-1]
        lists[n[1]-1] = temp
        s = "".join(lists)
        print(s)
    elif n[0] == "2":
        lists = list(s)
        for i in range(len(lists)):
            if lists[i] == n[1]:
                lists[i] = n[2]
        s = "".join(lists)
        print(s)