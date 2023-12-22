n = int(input())

numList = list(map(int, input().split()))
add = 0
for i in numList:
    if i < 100:
        add += i
    elif i > 100:
        add += i
        print(add)
        print("%.1f" % (add/n))
        break