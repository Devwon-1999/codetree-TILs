n = list(map(int, input()))
total = 0

for i in reversed(n):
    print(i, end="")
print(" ", end="")
for i in n:
    total += i

print(total)