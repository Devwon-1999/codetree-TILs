n = list(input())
n.reverse()
sum = 0
for i in n:
    print(i, end = "")

print(" ", end = "")

for i in n:
    i = int(i)
    sum += i

print(sum)