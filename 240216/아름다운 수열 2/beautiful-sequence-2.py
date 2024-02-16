# 순열 생성
def generate_permutations(arr, start, end, result):
    if start == end:
        result.append(arr[:])
    else:
        for i in range(start, end):
            arr[start], arr[i] = arr[i], arr[start]
            generate_permutations(arr, start + 1, end, result)
            arr[start], arr[i] = arr[i], arr[start]


N, M = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

permutations_B = []
generate_permutations(B, 0, M, permutations_B)

count = 0 # 정답

for i in range(N - M + 1): #부분 수열 확인
    subsequence = A[i:i+M]
    if subsequence in permutations_B:
        count += 1

print(count)