a, b = map(int, input().split())

hap = 0
for i in range(a, b+1):
    if i % 5 == 0:
        hap += i


print(hap)