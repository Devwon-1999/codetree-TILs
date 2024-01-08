n = int(input())

classAvgList = list(map(int, input().split()))

Aclass, Bclass = map(int, input().split())

sumOrder = classAvgList[Aclass - 1] + classAvgList[Bclass - 1]
avg = sumOrder / 2

print("%.1f" % avg)