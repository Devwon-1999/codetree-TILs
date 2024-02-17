N = int(input())

base = []

for i in range(N):
    temp = list(map(int, input().split()))
    base.append(temp)

max_cnt = 0
for i in range(N - 1):
    for j in range(N - 2):
        temp1 = 0
        temp2 = 0
        for k in range(3):
            temp1 += base[i][j + k]
            temp2 += base[i + 1][j + k]
        max_cnt = max(max_cnt, temp1 + temp2)
       
print(max_cnt)