n, m = tuple(map(int, input().split()))
answer = [
    [0 for _ in range(m)]
    for _ in range(n)
]
value = 1

for i in range(n + m - 2):
    for j in range(n):
        for k in range(m):
            if i == j + k and j < n and k < m:
                answer[j][k] += value
                value += 1
        

for i in range(n):
    for j in range(m):
        print(answer[i][j], end = " ")
    print()