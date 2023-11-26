arr = list(map(int, input().split()))
new = list()
cnt = 0
add = 0
for i in arr:
    if i == 0:
        break
    new.append(i)

for i in new:
    if i % 2 == 0:
        cnt += 1
        add += i

print(cnt, add)