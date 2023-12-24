n = int(input())

for i in range(n):
    temp = list(input())
    temp.reverse()
    for i in temp:
        print(i,end="")
    print()