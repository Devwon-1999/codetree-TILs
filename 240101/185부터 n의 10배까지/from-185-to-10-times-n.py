n = int(input())
sum = 0
cnt = 0
avg = 0
for i in range(185, n * 10 + 1):
    sum += i
    cnt += 1

avg = sum / cnt

print(sum, "%.1f" % avg)