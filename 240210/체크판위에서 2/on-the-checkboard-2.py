R, C = map(int, input().split())

check = [list(input().split()) for i in range(R)]

cnt = 0

for i in range(1, R):
    for j in range(1, C):
        for k in range(i + 1, R - 1):
            for l in range(j + 1, C - 1):
                if check[0][0] != check[i][j] and check[i][j] != check[k][l] and check[k][l] != check[R - 1][C - 1]:
                    cnt += 1

print(cnt)