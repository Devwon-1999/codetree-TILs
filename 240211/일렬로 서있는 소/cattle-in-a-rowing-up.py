N = int(input())

cow_place = []

for i in range(N):
    temp = int(input())
    cow_place.append(temp)

cnt = 0

for i in range(N):
    for j in range(i + 1, N):
        for k in range(j + 1, N):
            if j - i <= k - j and k - j <= 2 *(j - i):
                cnt += 1

print(cnt)