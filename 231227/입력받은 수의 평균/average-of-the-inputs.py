n = int(input())
sum = 0
for i in range(n):
    temp = int(input())
    sum += temp

print("%.1f" % (sum / n))

if sum / n < 70:
    print("fail")