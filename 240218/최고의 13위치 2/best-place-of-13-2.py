N = int(input())

base = []
for _ in range(N):
    temp = list(map(int, input().split()))
    base.append(temp)

max_cnt = 0

# 겹치지 않는 1x3 크기의 부분 격자에서 최대 동전 개수 계산
for i in range(N):
    for j in range(N - 2):
        # 첫 번째 1x3 부분 격자
        grid1 = base[i][j] + base[i][j+1] + base[i][j+2]
        
        # 두 번째 1x3 부분 격자를 현재 격자와 겹치지 않도록 배치
        for k in range(N):
            if k == i:  # 첫 번째 1x3 부분 격자와 겹치지 않도록 처리
                continue
            grid2 = base[k][j] + base[k][j+1] + base[k][j+2]
            max_cnt = max(max_cnt, grid1 + grid2)

            if max_cnt == 6:  # 최대값일 경우 종료
                print(max_cnt)
                exit()

print(max_cnt)