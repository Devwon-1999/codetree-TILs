n, m = map(int, input().split())
resultList = [
    [0 for _ in range(n)]
    for _ in range(n)
]
cnt = 1
for i in range(m):
    a, b = list(map(int, input().split()))
    resultList[a-1][b-1] = cnt
    cnt += 1

for i in range(n):
    for j in range(n):
        print(resultList[i][j], end = " ")
    print()