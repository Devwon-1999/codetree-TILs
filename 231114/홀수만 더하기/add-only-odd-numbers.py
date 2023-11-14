n = int(input())
a = list()
for i in range(n):
    m = int(input())
    a.append(m)

sum = 0
for i in a:
    if i % 3 == 0 and i % 2 == 1:
        sum += i
print(sum)