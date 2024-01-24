N, B = map(int, input().split())
result = []
while N > 0:
    digit = N % 4
    N = N // 4
    result.append(digit)

for i in range(len(result) - 1, -1, -1):
    print(result[i], end = "")