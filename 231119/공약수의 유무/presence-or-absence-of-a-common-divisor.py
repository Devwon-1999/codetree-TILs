a, b = map(int, input().split())
count = 0
for i in range(a, b+1):
    if 1920 % i == 0 and 2880 % i == 0:
        count += 1
    else:
        continue
if count >= 1:
    print(1)
else:
    print(0)