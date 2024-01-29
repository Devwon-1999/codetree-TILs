N, M, K = map(int, input().split())

result = [0 for i in range(N)]
answer = []
for i in range(M):
    student = int(input())

    result[student - 1] += 1

for i in result:
    if i >= K:
        answer.append(i)
        print(result.index(max(result)) + 1)

if answer:
    pass
else:
    print(-1)