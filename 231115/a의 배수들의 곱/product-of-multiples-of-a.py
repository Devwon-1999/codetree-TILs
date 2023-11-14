a, b = map(int, input().split())
gop = 1
for i in range(1, b+1):
    if i % a == 0:
        gop *= i

print(gop)