a, b = map(int, input().split())
c, d = map(int, input().split())

base = [0 for i in range(101)]

for i in range(a, b):
    base[i] += 1

for i in range(c, d):
    base[i] += 1

cnt = 0
for i in base:
    if i >= 1:
        cnt += 1
print(cnt)