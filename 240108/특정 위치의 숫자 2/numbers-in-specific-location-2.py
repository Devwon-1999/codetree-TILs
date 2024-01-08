n = int(input())

numList = list(map(int, input().split()))

hap = 0
cnt = 0
for i in range(1, len(numList), 2):
    hap += numList[i]
    cnt += 1

print(hap, "%.1f" % (hap / cnt))