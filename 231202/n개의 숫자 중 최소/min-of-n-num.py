n = int(input())

arr = list(map(int, input().split()))
cnt = 0
for i in arr:
    if min(arr) == i:
        cnt += 1

print(min(arr), cnt)