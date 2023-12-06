# n = int(input())

# answer = [
#     [0 for _ in range(n)]
#     for _ in range(n)
# ]
# num = 1
# for i in range(n-1, -1, -1):
#     for j in range(n-1, -1, -1):
#         answer[i][j] = num
#         num += 1

# for i in range(n):
#     for j in range(n):
#         print(answer[i][j], end = " ")
#     print()

# 격자 크기 입력 받기
n = int(input())

# 격자 초기화
arr = [[0] * n for _ in range(n)]

# 시작 숫자 설정
num = n * n


for j in range(n):
    if j % 2 == 0:
        for i in range(n - 1, -1, -1):
            arr[i][j] = num
            num -= 1
    else:
        for i in range(n):
            arr[i][j] = num
            num -= 1

# 결과 출력
for i in range(n):
    print(*arr[i])