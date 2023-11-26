arr = list(map(int, input().split()))

evenSum = 0
threemul = 0
for i in range(0, 10):
    if i % 2 == 1:
        evenSum += arr[i]

    if i % 3 == 2:
        threemul += arr[i]

print(evenSum, "%.1f" % (threemul/3))