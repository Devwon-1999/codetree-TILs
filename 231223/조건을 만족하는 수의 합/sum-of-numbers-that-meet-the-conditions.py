n = int(input())
sum = 0
for i in range(n, 501):
    if i % 2 == 0:
        sum += i
print(sum)