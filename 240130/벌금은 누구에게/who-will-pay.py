N, M, K = map(int, input().split())
#N 학생 수 M 걸린 학생 K 벌칙 횟수 제한
result = [0 for i in range(N)]
answer = []
for i in range(M):
    student = int(input())
    result[student - 1] += 1
    for j in result:
        if j >= K:
            answer.append(result.index(max(result)) + 1)
            break
    if answer:
        break

if answer:
    print(answer[0])
else:
    print(-1)