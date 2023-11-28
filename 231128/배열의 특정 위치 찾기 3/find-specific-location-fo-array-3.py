arr = list(map(int, input().split()))
cnt = 0
add = 0
for i in arr:
    if i == 0:
        break
    cnt += 1

for i in range(cnt):
    add += arr[i]

print(add)