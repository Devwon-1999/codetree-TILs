n = int(input())
a = list()
for i in range(n):
    num = int(input())
    a.append(num)

for i in a:
    if i % 2 == 1 and i % 3 == 0:
        print(i)