n = int(input())

numList = list(map(int, input().split()))
add = 0
for i in numList:
        add += i

print(add)
print("%.1f" % (add/n))