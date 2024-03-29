N, K = map(int, input().split())
base = [0 for i in range(101)]

for i in range(N): # 위치, 사탕 개수 셋팅
    candy, index = map(int, input().split())
    base[index - 1] = candy


result = [] #결과 리스트
for i in range(K, 100 - K): #메인 알고리즘
    candy_cnt = 0
    for j in range(i - K, i + K + 1): # 중심점으로부터 C - K ~ C + K 까지
        candy_cnt += base[j]
    result.append(candy_cnt)

print(max(result))