n = int(input())

hap = 0
for i in range(n):
    m = int(input())
    hap += m

print(hap, "%.1f" % (hap/n))