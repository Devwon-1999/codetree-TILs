n = int(input())
cow_height = list(map(int, input().split()))

cnt = 0

for i in range(n):
    for j in range(i + 1, n):
        for k in range(j + 1, n):
            if cow_height[i] <= cow_height[j] <= cow_height[k]:
                cnt += 1

print(cnt)