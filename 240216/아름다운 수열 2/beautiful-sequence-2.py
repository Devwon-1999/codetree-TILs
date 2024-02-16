# 입력 받기
N, M = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

# B의 각 숫자가 몇 개씩 있는지를 저장
counts_B = {}
for num in B:
    if num in counts_B:
        counts_B[num] += 1
    else:
        counts_B[num] = 1

count = 0

for i in range(N - M + 1): #부분 수열 확인
    subsequence = A[i:i+M]
    counts_subsequence = {}
    for num in subsequence:
        if num in counts_subsequence:
            counts_subsequence[num] += 1
        else:
            counts_subsequence[num] = 1
    if counts_subsequence == counts_B:
        count += 1

print(count)