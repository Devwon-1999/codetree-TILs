N = int(input())

base = []

for i in range(N):
    temp = list(map(int, input().split()))
    base.append(temp)

max_cnt = 0
for i in range(N):
    for j in range(N - 2):
        temp = 0
        for k in range(3):
            temp += base[i][j + k]
        max_cnt = max(max_cnt, temp)
       
print(max_cnt)