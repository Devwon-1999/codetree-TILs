arr = list(map(int, input().split()))
cnt = 0
add = 0
for i in arr:
    if i >= 250:
        break
    cnt += 1

for i in range(0, cnt):
    add += arr[i]

print(add, end=" ")
print("%.1f" %(add/cnt))