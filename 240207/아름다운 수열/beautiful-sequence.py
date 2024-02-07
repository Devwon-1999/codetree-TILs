N = int(input())
N_List = []
for i in range(N):
    temp = int(input())
    N_List.append(temp)

M = int(input())
M_List = []
for i in range(M):
    temp = int(input())
    M_List.append(temp)

result = []

cnt = 0
for i in range(N - M + 1):
    subsequence = N_List[i : i + M]
    if set(subsequence) == set(M_List):
        cnt += 1
        result.append(i+1)  # 인덱스는 1부터 시작하므로 +1
    else:
        diff = subsequence[0] - M_List[0]
        beautiful = True
        for j in range(1, M):
            if subsequence[j] - M_List[j] != diff:
                beautiful = False
                break
        if beautiful:
            cnt += 1
            result.append(i+1)

print(cnt)
for idx in result:
    print(idx)