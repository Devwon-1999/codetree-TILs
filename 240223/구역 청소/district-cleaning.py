a, b = map(int, input().split())
c, d = map(int, input().split())

min_val = 0
if a > c:
    min_val = c 
else:
    min_val = a

max_val = 0
if b > d:
    max_val = b
else:
    max_val = d

cnt = 0
for i in range(min_val, max_val):
    cnt += 1

print(cnt)