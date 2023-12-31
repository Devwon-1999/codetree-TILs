N, P = map(int, input().split())
result = []
cnt = 0
for i in range(100):
    N = (N * N) % P
    result.append(N)
    
for i in range(1, 100):
    cnt += 1
    if result[0] == result[i]:
        print(cnt + 1)
        break