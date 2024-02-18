N = int(input())

base = []

for i in range(N):
    temp = list(map(int, input().split()))
    base.append(temp)

max_cnt = 0
for i in range(N):
    for j in range(N - 2):
        for k in range(i + 2, N):
            for l in range(N - 2):
                max_cnt = max(max_cnt, base[i][j] + base[i][j + 1] + base[k][l] + base[k][l + 1])

for i in range(N - 1):
    for j in range(N - 2):
        temp1 = 0
        temp2 = 0
        for k in range(3):
            temp1 += base[i][j + k]
            temp2 += base[i + 1][j + k]
        max_cnt = max(max_cnt, temp1 + temp2)

for i in range(N):
    for j in range(N - 5):
        temp = 0
        for k in range(6):
            temp += base[i][j + k]
        max_cnt = max(max_cnt, temp)

print(max_cnt)