N, K = map(int, input().split())
base = [0 for i in range(101)]
index_List = []
for i in range(N): # 위치, 사탕 개수 셋팅
    candy, index = map(int, input().split())
    if base[index-1] == 0:
        base[index - 1] = candy
    else:
        base[index - 1] += candy
    print(base[index - 1])

result = [] #결과 리스트
for i in range(N): #메인 알고리즘
    candy_cnt = 0
    if i - K < 0 and i + K >= 100:
        continue
    for j in range(i - K, i + K + 1): # 중심점으로부터 C - K ~ C + K 까지
            candy_cnt += base[j]
    result.append(candy_cnt)

print(result)