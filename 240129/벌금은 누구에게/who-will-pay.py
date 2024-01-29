N, M, K = map(int, input().split())

result = [0 for i in range(N)]

for i in range(M):
    student = int(input())

    result[student-1] += 1

print(result.index(max(result)) + 1)