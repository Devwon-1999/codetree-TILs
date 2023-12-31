x, y = map(int, input().split())
sum = 0
avg = 0
cnt = 0
if x > y:
    for i in range(y, x + 1):
        if i % 5 != 0:
            sum += i
            cnt += 1
else:
    for i in range(x, y + 1):
        if i % 5 != 0:
            sum += i
            cnt += 1
avg = sum / cnt

print(sum, "%.1f" % avg)